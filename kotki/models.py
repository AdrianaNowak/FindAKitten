from django.db import models


class Cat(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"Kot {self.name}, kolor sierści: {self.color}, urodzony:{self.date_of_birth}"


class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} with age: {self.age}"


class Image(models.Model):
    name = models.CharField(max_length=50)
    main_Img = models.ImageField(upload_to='images/')
