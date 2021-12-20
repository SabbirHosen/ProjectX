from . import views
from django.urls import path, include


urlpatterns = [
   path('', views.login, name='login'),
   path('registration/', views.registration, name='registration'),

]