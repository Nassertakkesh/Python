from django.db import models
from datetime import *
from django.contrib import messages
import bcrypt

import re	# the regex module

class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = ("Invalid email address!")
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name should be at least 2 characters"
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 8 characters"
        if datetime.strptime(postData['birth_date'], "%Y-%m-%d") > datetime.today():
            errors["birth_date"] = "BirthDate should be in the past"
        if user.objects.filter(email=postData['email']):
            errors["email"] = "email is taken"
        if (postData['password']) != (postData['password_confirm']):
            errors["password"] = "Password's should match"
        return errors

    def loginValid(self, request):
        theuser = user.objects.filter(email=request.POST['email']) 
        if theuser: 
            logged_user = theuser[0] 
            if not bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                messages.error(request, "Invalid credentials")
            else:
                return True
        messages.error(request, "Invalid credentials")
        return False

class user(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=255)
    password_confirm = models.CharField(max_length=255)
    birth_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlogManager()   

    def __repr__(self):
        return f"<Book object: {self.title} {self.desc}({self.id})>"



# Create your models here.
