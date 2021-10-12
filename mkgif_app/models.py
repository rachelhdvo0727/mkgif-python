from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
import django_rq
from .utils import mk_gif_ffmpeg

class Animation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def enqueue(self, params):
        django_rq.enqueue(mk_gif_ffmpeg, {
            'pk': self.pk,
            'params': params,
            }
        )

    # Showing readable name in admin page
    def __str__(self):
        return f"{self.name}"


class Image(models.Model):
    def image_path(self, filename):
        # Return a file path str, that we want to save the image to
        return f'{self.animation.pk}/{filename}'

    animation = models.ForeignKey('Animation', on_delete=models.CASCADE)
    # Take image_path function and upload the image's path to the file
    image = models.ImageField(upload_to=image_path)

    @property
    def media_url(self):
        return f'{ settings.MEDIA_URL }{ self.image }'
