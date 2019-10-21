from django.shortcuts import render,redirect, HttpResponse
import random 
from .models import *


def index(request):
    context = {
        "allbooks": book.objects.all()
    }
    return render(request, "booksAuthorsApp/index.html", context)

#***************************************************************************************************
def add_books(request):
    print("add_books")
    print(request.POST["book"])
    print(request.POST["descrip"])
    currBook = book.objects.create(title=request.POST["book"], desc=request.POST["descrip"])
    return redirect("/books")
#***************************************************************************************************
def books(request):
    context = {
        "allbooks": book.objects.all()
    }
    return render(request, "booksAuthorsApp/index.html", context)

#***************************************************************************************************
def book_page(request,bookid):
    print("add_authors")
    context = {
        "currentbook": book.objects.get(id=bookid),
        "allauthors": author.objects.all(),
        "authors": author.objects.all().exclude(books__in=book.objects.filter(id=int(bookid)))
    }
    return render(request, "booksAuthorsApp/book_page.html",context)


#***************************************************************************************************

def addingauthor(request):
    print("addingbooks")
    bookid = request.POST['bookid']
    authorid = request.POST['authorsid']
    print(bookid)
    print(request.POST)
    print("dude lets check this out")
    that_author = author.objects.get(id = authorid)
    that_book = book.objects.get(id= bookid)
    that_book.booking.add(that_author)

    return redirect("/books/"+bookid)





#**************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************


def add_authors(request):
    if request.method == "POST":
        print("add_authors")
        print(request.POST["first_name"])
        print(request.POST["last_name"])
    currAuthor = author.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], notes=request.POST["notes"])
    return redirect("/authors")

#***************************************************************************************************

def authors(request):
    context = {
        "allauthors": author.objects.all()
    }
    return render(request, "booksAuthorsApp/authors.html", context)

#***************************************************************************************************
def reset(request):

    deleting= book.objects.all()	# let's retrieve a single movie,
    deleting.delete()
    deleting2= author.objects.all()	# let's retrieve a single movie,
    deleting2.delete()

    return render(request, "booksAuthorsApp/index.html")
#***************************************************************************************************
def authors_page(request,authid):
    print("add_authors")
    context = {
        "allauthors": book.objects.all(),
        "currentAuthor" :  author.objects.get(id=authid),
        "books": book.objects.all().exclude(booking__in=author.objects.filter(id=int(authid)))
    }

    return render(request, "booksAuthorsApp/authors_page.html",context)
#***************************************************************************************************
def addingbook(request):
    print("addingbooks")
    bookid = request.POST['jake']
    authorid = request.POST['authorsid']
    print(bookid)
    print(request.POST)
    print("helloooosojvojve")
    this_author = author.objects.get(id = authorid)
    this_book = book.objects.get(id= bookid)
    this_author.books.add(this_book)

    return redirect("/authors/"+authorid)

