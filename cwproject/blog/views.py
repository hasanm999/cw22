from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView


# Create your views here.
class ContactView(ListView):
    template_name = 'parent/contact_us.html'


class HomeView(ListView):
    template_name = 'parent/home.html'


class AboutView(ListView):
    template_name = 'parent/about.html'

