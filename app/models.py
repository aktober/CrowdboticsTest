from django.db import models
from django.contrib.auth.models import User


class Owner(models.Model):
    name = models.CharField(max_length=15)
    user = models.OneToOneField(User, null=True)

    def __str__(self):
        return self.name


class Dog(models.Model):
    name = models.CharField(max_length=15)
    birthday = models.DateField()
    owner = models.ForeignKey(Owner)

    def __str__(self):
        return self.name


class Cat(models.Model):
    name = models.CharField(max_length=15)
    birthday = models.DateField()
    owner = models.ForeignKey(Owner)

    def __str__(self):
        return self.name




