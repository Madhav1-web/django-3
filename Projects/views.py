from django.shortcuts import render
from django.http import HttpResponse
import random
from .models import Project

# Create your views here.

def home(request):
	projects=Project.objects.all()
	return render(request, 'Projects/home.html', {'projects':projects})