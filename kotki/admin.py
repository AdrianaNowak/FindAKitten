from django.contrib import admin

from .models import Animal, Person, Image

admin.site.register(Animal)
admin.site.register(Person)
admin.site.register(Image)
