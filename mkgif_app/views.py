from django.shortcuts import render, get_object_or_404
from .models import Animation, Image
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from redis import Redis
import django_rq
from rq import Queue, Worker

@login_required
def index(request):
    # If we get a POST req, create an Animation obj instance
    if request.method == 'POST':
        # AFTER setting up user account
        anim = Animation.objects.create(name=request.POST['name'], user_id=request.user.id)

        # Loop through any images submitted
        for img in request.FILES.getlist('imgs'):
            # Save submitted images with the anim obj
            Image.objects.create(animation=anim, image=img)

    # Show a list of all Animation (without user)
    # anims = Animation.objects.all()

    # Show a list of all exisiting animations of the logged in user
    anims = Animation.objects.filter(user=request.user)
    context = {
            'anims': anims
            }
    return render(request, 'mkgif/index.html', context)

@login_required
def details(request, pk):
    anim = get_object_or_404(Animation, pk=pk)
    images = Image.objects.filter(animation=pk)

    # Use django_rq's Queue() to connect with Redis
    queue = Queue(connection=Redis())
    # Get Animation object with pk
    frames = Animation.objects.get(pk=pk)
    # Attach Animation obj to rqworker's .enqueue() method
    gif = frames.enqueue({})

    context = {
            'anim': anim,
            'images': images,
            'gif': gif,
            }
    return render(request, 'mkgif/details.html', context)

@login_required
def delete_anim(request, pk):
    #pk = request.POST.get('pk', 3)
    anim = get_object_or_404(Animation, pk=pk)
    anim.delete()

    # HttpResponseRedirect for staying on the same page
    return HttpResponseRedirect(reverse('mkgif_app:index'))



