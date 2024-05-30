from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# Create your views here.
class ContactView(View):
    template_name = 'contact_us.html'

    def get(self, request):
        return render(request, self.template_name)


class HomeView(View):
    template_name = 'home.html'

    def get(self, request):
        return render(request, self.template_name)


class AboutView(View):
    template_name = 'about.html'

    def get(self, request):
        return render(request, self.template_name)


class ColorsView(View):
    template_name = ''
    def get(self, request):
        color = self.kwargs['color_name']
        if color == 'red':
            self.template_name = 'red.html'
            return render(request, self.template_name)
        elif color == 'blue':
            self.template_name = 'blue.html'
            return render(request, self.template_name)

