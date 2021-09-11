from django.shortcuts import redirect, render, HttpResponse
from django.urls.conf import path
def index(request):
   return HttpResponse("Placeholder to later display a list of all blogs.")

def newz(request):
   return HttpResponse("Placeholder to display a new form to create a new blog")

def create(request):
   return redirect('/')

def show(request, num):
   return HttpResponse(f"Placeholder to display blog {num}.")

def edit(request, num):
   return HttpResponse(f"Placeholder to edit blog {num}.")

def destroy(request, num):
   return redirect('/')