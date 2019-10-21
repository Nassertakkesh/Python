from django.shortcuts import render, HttpResponse,redirect	# notice the import!
from django.utils.crypto import get_random_string

def index(request):
    request.session["counter"] = -1
    return redirect ("/random_word")

def random_word(request):
    context = {
        'unique_id' : get_random_string(length=14)
    }
    request.session["counter"] += 1
    return render(request, "randomWordApp/index.html", context)

def randomGen(request):
    print('hello')
    if request.method == "POST" or "GET":
        print("hello")    
    return redirect ("/random_word")


def reset(request):
    print('hello')
    request.session["counter"] = -1
    return redirect ("/random_word")

