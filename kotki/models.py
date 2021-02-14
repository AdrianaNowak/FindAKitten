from django.db import models


class Animal(models.Model):
    type = models.CharField(max_length=25)
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.type} o imieniu {self.name}"


class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} with age: {self.age}"


class Image(models.Model):
    name = models.CharField(max_length=50)
    main_Img = models.ImageField(upload_to='images/')
