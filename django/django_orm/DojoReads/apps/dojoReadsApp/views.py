
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt


def register(request):
    errors = User.objects.basic_validator(request.POST)
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
        var = User.objects.create(name=request.POST['name'], alias=request.POST['alias'], password=pw_hash, password_confirm=pw_hash_confirm, email=request.POST['email']) 
        print("its working")
        print(var)

        return redirect("/book")
        
def login(request):
    if not User.objects.loginValid(request):
        return redirect('/')
    else:
        theuser = User.objects.filter(email=request.POST['email']) 
        if theuser: 
            logged_user = theuser[0] 
            request.session['userid'] = logged_user.id
            return redirect('/book')
        return redirect('/')

def index(request):
    if request.session.get("userid"):
        return redirect("/book")
    return render(request,"dojoReadsApp/index.html")

def logout(request):
    del request.session['userid'] 
    return redirect("/")


def presuccess(request):
    uid = request.session.get("userid")
    if not uid:
        return redirect("/")
    context = {
        "thisuser" : User.objects.get(id=uid),
        "allbooks" : Book.objects.all(),
        "this_user" : User.objects.get(id=uid)

    }
    return render(request,"dojoReadsApp/success.html",context)



def addingbook(request):
    errors = User.objects.book_add_valid(request)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/book')
    else:
        if request.session.get("userid"):
            this_user_session_id = request.session.get("userid")
            print(this_user_session_id)
            this_user_obj= User.objects.get(id= this_user_session_id)
            print(this_user_obj.first_name)
            # print(for key in )
            new_book_adding = Book.objects.create(title=request.POST["titleName"],desc=request.POST["descriptionName"],uploaded_by = this_user_obj)
            print(new_book_adding)
            this_user = User.objects.get(id=this_user_session_id)
            print(this_user)
            new_book_adding.users_who_fav.add(this_user)
            return redirect ("/book")
        return render(request,"dojoReadsApp/index.html")

