from django.urls import path
from .views import *

urlpatterns = [
    # path('', HomeView.as_view, name='home'),
    path('contact/', ContactView.as_view, name='contact_us'),
    path('about/', AboutView.as_view, name='about'),
    path('<str:color_name>/', ColorsView.as_view, name='color')
]

