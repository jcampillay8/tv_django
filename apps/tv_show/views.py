from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


def tvshow(request):
    ctx = {
        'shows': Show.objects.all()
    }    
    return render(request,'tvshow/home.html', ctx)


def new_show(request):
    return render(request, "tvshow/add_show.html")

def create(request):
    errors = Show.objects.validator(request.POST)
    if len(errors)> 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/tvshow/new_show')
    show = Show.objects.create(title=request.POST['title'], network=request.POST['network'],release_date=request.POST['release_date'], description=request.POST['description'])
    messages.success(request, "Show succesfullt created")
    return redirect(f'/tvshow/{show.id}')

def show (request, id):
    ctx ={
        'show':Show.objects.get(id=id)
    }
    return render(request, "tvshow/show.html", ctx)

def edit_show(request, id):
    ctx ={
        'show':Show.objects.get(id=id)
    }
    return render(request, "tvshow/edit_show.html", ctx)

def destroy(request, id):
    Show.objects.get(id=id).delete()
    return redirect("/tvshow/tvshow")


def update(request):
    errors = Show.objects.validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request.value)
        return redirectf(f'/tvshow/{id}/edit')
    else:
        u = Show.objects.get(id=request.POST['id'])
        u.title = request.POST['title']
        u.network = request.POST['network']
        u.release_date = request.POST['release_date']
        u.description = request.POST['description']
        u.save()
        return redirect("/tvshow/"+str(u.id))