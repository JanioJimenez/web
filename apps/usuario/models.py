# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class UserMethods:
    def initial(self):
        return self.username[0].upper()

    def fname(self):
        return '{} {}'.format(self.first_name, self.last_name)


class User(AbstractUser, UserMethods):
	age = models.IntegerField(null=True, blank=True)
	city = models.ForeignKey(City, null=True, blank=True, on_delete=models.CASCADE)
	language = models.ForeignKey(Language, null=True, blank=True, on_delete=models.CASCADE)
	provider = models.CharField(max_length=20, null=True, blank=True)


class Code(models.Model):
    name = models.CharField(max_length=30)
    code = models.BinaryField()
    description = models.CharField(max_length=50)
    compilations = models.IntegerField(default=0)
    creation_date = models.DateField(auto_now=True)
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return "{}  ({})".format(self.user.username, self.name)
