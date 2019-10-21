from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages

def shows(request):

    context={
        "Shows" : Shows.objects.all()
    }

    return render(request, "restfulShowsApp/shows.html",context)



def new_show(request):
    return render(request, "restfulShowsApp/new_show.html")



def add_new_show(request):
    errors = Shows.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/shows/new")
    else:
        print("lets see if this works -- adding new show")
        new_show = Shows.objects.create(title =request.POST["titleName"], network = request.POST["networkName"], description = request.POST["descriptionName"], release_date = request.POST["dateName"])
        print(new_show)
        newshowid = new_show.id
        print(newshowid)
        return redirect("/shows/" + str(newshowid))

def edit_show(request,id):
    if request.method == "GET":

        context= {
        "show": Shows.objects.get(id=id)
        }
        return render(request, "restfulShowsApp/edit_show.html",context)

    if request.method == "POST":
        errors = Shows.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/shows/" + id +"/edit")
        else:
            print("lets see if this works -- updating show")
            updating_show = Shows.objects.get(id=id)
            print(updating_show.title)
            updating_show.title = request.POST["titleName"]
            updating_show.network = request.POST["networkName"]
            updating_show.description = request.POST["descriptionName"]
            updating_show.release_date = request.POST["dateName"]
            print(updating_show)
            updating_show.save()
        return redirect("/shows/" + id )


# movie_to_update = Movie.objects.get(id=42)	# let's retrieve a single movie,
# movie_to_update.description = "the answer to the universe"	# update one/some of its field values
# movie_to_update.title = "The Hitchhiker's Guide to the Galaxy"
# movie_to_update.save()	# then make sure all changes to the existing record get saved to the database

    return render(request, "restfulShowsApp/edit_show.html")



def shows_page(request,id):
    context={
        "ShowPage" : Shows.objects.get(id =id)
    }

    return render(request, "restfulShowsApp/shows_page.html",context)


def delete_show(request,id):
        print("lets see if this works -- deleting show")
        deleteing = Shows.objects.get(id=id)
        deleteing.delete()
        return redirect("/shows")