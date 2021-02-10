from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory

from .models import Person, Cat


def detail(request, id):
    person = get_object_or_404(Person, pk=id)
    return render(request, "kotki/detail.html", {"person": person})


def cats_list(request):
    return render(request, "kotki/cats_list.html", {"cats": Cat.objects.all()})


PersonForm = modelform_factory(Person, exclude=[])
CatForm = modelform_factory(Cat, exclude=[])


def new_person(request):
    if  request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = PersonForm()
    return render(request, "kotki/new_person.html", {"form": form})


def new_cat(request):
    if request.method == "POST":
        form = CatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = CatForm()
    return render(request, "kotki/new_cat.html", {"form": form})
