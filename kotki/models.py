from django.db import models


class Cat(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"Cat {self.name} with color: {self.color} born: {self.date_of_birth}"


class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} with age: {self.age}"
