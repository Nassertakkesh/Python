from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import user
import bcrypt

def index(request):
    if request.session.get("userid"):
        return redirect("/presuccess")
    return render(request,"LoginRegistrationApps/index.html")

def success(request):
    uid = request.session.get("userid")

    if not uid:
        return redirect("/")
    return redirect("/presuccess")

def register(request):
    errors = user.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        password = request.POST['password']
        print(password)
        password_confirm = request.POST['password_confirm']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()) 
        pw_hash_confirm = bcrypt.hashpw(password_confirm.encode(), bcrypt.gensalt()) 
        print(pw_hash)
        user.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], password=pw_hash, password_confirm=pw_hash_confirm, 
        email=request.POST['email'], birth_date=request.POST['birth_date']) 
        print("its working")

        return redirect("/presuccess")

def presuccess(request):
    uid = request.session.get("userid")
    if not uid:
        return redirect("/")
    context = {
        "thisuser" : user.objects.last()
    }
    return render(request,"LoginRegistrationApps/success.html",context)


def login(request):
   
    if not user.objects.loginValid(request):
        return redirect('/')
    else:
        theuser = user.objects.filter(email=request.POST['email']) 
        if theuser: 
            logged_user = theuser[0] 
            request.session['userid'] = logged_user.id
            return redirect('/presuccess')
        return redirect('/')
    


def logout(request):
    del request.session['userid'] 
    return redirect("/")


    #filter instead of get bc if get empty then crash# note that we take advantage of truthiness here: an empty list will return false # assuming we only have one user with this username, the user would be first in the list we get back
    # of course, we should have some logic to prevent duplicates of usernames when we create users
    # use bcrypt's check_password_hash method, passing the hash from our database and the password from the form
    # if we get True after checking the password, we may put the user id in session
    # never render on a post, always redirect!
    # if we didn't find anything in the database by searching by username or if the passwords don't match, 
    # redirect back to a safe route


