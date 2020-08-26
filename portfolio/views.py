from django.shortcuts import render

# Create your views here.
from .models import Portfolio

def home(request):
    projects = Portfolio.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})
