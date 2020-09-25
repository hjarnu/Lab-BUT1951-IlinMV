from django.shortcuts import render
from django.http import HttpResponse
from django import template
from .models import Article
def home(request):
	return render(request, 'templates/archive.html')
def archive(request):
	return render(request, 'archive.html', {"posts": Article.objects.all()})
# Create your views here.
