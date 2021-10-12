from django.urls import path
from . import views

# App's name from inside the templates
app_name = 'mkgif_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:pk>/', views.details, name='details'),
    path('delete_anim/<int:pk>/', views.delete_anim, name='delete_anim'),
]
