from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from kotki.models import Person


def welcome(request):
    return render(request, "website/welcome.html", {"people": Person.objects.all()})


def date(request):
    return HttpResponse("wynik datetime now : " + str(datetime.now()))


def jakistrzeciprzyklad(request):
    return HttpResponse("baps!")



# Person.objects.all() zwraca wszystkie rekordy z bazy