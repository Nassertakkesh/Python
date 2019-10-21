from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def one_method(request):
    return HttpResponse("BEAR")     

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect("/") 

def number(request,numbs):
    return HttpResponse(f"placeholder to display a blog {numbs}")
 
def edit(request, numbs):
    return HttpResponse(f"placeholder to edit blog  {numbs}")

def destroy(request,numbs):
    return redirect("/") 
