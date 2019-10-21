from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt


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

def index(request):
    if request.session.get("userid"):
        return redirect("/presuccess")
    return render(request,"LoginRegistrationApps/index.html")

def presuccess(request):
    uid = request.session.get("userid")
    if not uid:
        return redirect("/")
    context = {
        "thisuser" : user.objects.last()
    }
    return render(request,"LoginRegistrationApps/success.html",context)

def logout(request):
    del request.session['userid'] 
    return redirect("/")



################^^^^^^^^^^^THE ABOVE CODE IS FOR REGISTRATION AND LOGIN^^^^^^^^^^^^######################

def thewall(request):
    if request.session.get("userid"):
        context={
            "pulling_comment_data" : Comment.objects.all(),
            "pulling_post_data" : Post.objects.all().order_by("-created_at")
        }
        return render(request,"LoginRegistrationApps/thewall.html",context)
    return render(request,"LoginRegistrationApps/index.html")

   # post_id.filter(post_id=request.POST['post_id']).order_by("created_at"),

def post(request):
    if request.session.get("userid"):
        this_user_id = request.session.get("userid") 
        this_user = user.objects.get(id=this_user_id)
        creatingpost = Post.objects.create(message = request.POST["post"],users = this_user)
        print("we made a post")
        print(creatingpost)
        # context={
        #     "pulling_data" : Post.objects.all().order_by("-created_at")
        # }
        # return render(request,"LoginRegistrationApps/thewall.html",context)
        return redirect("/thewall")
    return render(request,"LoginRegistrationApps/index.html")


def comment(request):
    if request.session.get("userid"):
        this_post_id = request.POST['comment_id'] 
        this_post = Post.objects.get(id= this_post_id)
        this_user_id = request.session.get("userid") 
        this_user = user.objects.get(id=this_user_id)
        print(this_post)
        print(this_post_id)
        print(this_user)
        print(this_user_id)
        creatingcomment = Comment.objects.create(comment = request.POST["comment"],post_id=this_post,user_id=this_user)
        print("we made a post")
        print(creatingcomment)
        # context={
        #     "comment_data" : Comment.objects.all().order_by("created_at")
        # }
        # return render(request,"LoginRegistrationApps/thewall.html",context)
        return redirect("/thewall")
    return render(request,"LoginRegistrationApps/index.html")


def delete(request):
    if request.session.get("userid"):
        print("HEHBFJBJSBCIBJHBJHBJBJBKBKJBKJFNDKJC KSNCBISBFJNSFNHSBHFBHB ")
        this_comment_id = request.POST['commentingid'] 
        print(this_comment_id)
        print("HEHBFJBJSBCIBJHBJHBJBJBKBKJBKJFNDKJC KSNCBISBFJNSFNHSBHFBHB ")
        comment_delete = Comment.objects.get(id= this_comment_id)
        comment_delete.delete()
        print("DONE")

        return redirect("/thewall")
    return render(request,"LoginRegistrationApps/index.html")
