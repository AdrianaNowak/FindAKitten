from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory
from django.http import HttpResponse
from .forms import *

from .models import Person, Animal, Image


def detail(request, id):
    person = get_object_or_404(Person, pk=id)
    return render(request, "kotki/detail.html", {"person": person})


def animals_list(request):
    return render(request, "kotki/animals_list.html", {"cats": Animal.objects.all()})


PersonForm = modelform_factory(Person, exclude=[])
AnimalForm = modelform_factory(Animal, exclude=[])


def new_person(request):
    if  request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = PersonForm()
    return render(request, "kotki/new_person.html", {"form": form})


def new_animal(request):
    if request.method == "POST":
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = AnimalForm()
    return render(request, "kotki/new_animal.html", {"form": form})


def new_image_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        name = request.POST.get('name')
        if form.is_valid():
            form.save()
            # odpowiedz = ML.RobieRzeczyIZwracamString
            odpowiedz = "Cat"
            if odpowiedz == "Dog":
                return redirect('theanswerPies', animal=name)
            if odpowiedz == "Cat":
                return redirect('theanswerKot', animal=name)
    else:
        form = ImageForm()
    return render(request, 'kotki/images.html', {'form': form})


def theanswerPies(request, animal):
    imageName = Image.objects.get(name=animal)
    return render(request, 'kotki/theanswerPies.html', {'animal': imageName})


def theanswerKot(request, animal):
    imageName = Image.objects.get(name=animal)
    return render(request, 'kotki/theanswerKot.html', {'animal': imageName})


def display_animal_images(request):
    images = Image.objects.all()
    return render(request, 'kotki/display_animal_images.html', {'animalImages': images})
