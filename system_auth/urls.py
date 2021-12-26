from . import views
from django.urls import path, include


urlpatterns = [
   path('', views.user_login, name='login'),
   path('registration/', views.registration, name='registration'),
   path('verify/<otp>', views.verify, name='verify'),
   path('profile/', views.profile, name='profile'),
   path('logout/', views.user_logout, name='logout'),
   path('success/<otp>', views.success, name='success'),




]