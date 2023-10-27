from django.urls import path
from . import views


urlpatterns = [

  path('',views.home,name='index'),
  path('home',views.home,name='index'),
  path('about',views.about,name='about'),
  path('location',views.location,name='location'),
  path('games',views.games,name='games'),
  path('signup',views.register,name='register'),
  path('login',views.loginview,name='login'),
  path('logged',views.logged,name='logged'),
  path('booking',views.booking,name='booking'),
  path('booked',views.booked,name='booked'),



]