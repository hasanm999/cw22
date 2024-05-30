from django.urls import path
from blog.views import *

path('contact/', ContactView.as_view, name='contact_us'),
path('home/', HomeView.as_view, name='home'),
path('about/', AboutView.as_view, name='about')
