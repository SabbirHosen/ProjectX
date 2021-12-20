from . import views
from django.urls import path, include


urlpatterns = [
   path('upload/', views.upload, name='upload'),
]