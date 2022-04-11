from django.db import models
import typing

from django.utils.datetime_safe import datetime


class Actor(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    sex = models.CharField(null=True, blank=True, max_length=6, choices=[("Man", "Man"),
                                                                         ("Woman", "Woman"),
                                                                         ("Other", "Other"),
                                                                         ])
    birthdate = models.DateTimeField(default=datetime.now)


class Category(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    ratingStars = models.IntegerField(null=True, blank=True, choices=[(1, "☆"),
                                                                      (2, "☆☆"),
                                                                      (3, "☆☆☆"),
                                                                      (4, "☆☆☆☆"),
                                                                      (5, "☆☆☆☆☆"), ])
    ratingPercentage = models.FloatField(null=True, blank=True)
    director = models.ForeignKey('Director', null=True, blank=True, on_delete=models.CASCADE)
    actors = models.ManyToManyField('Actor', blank=True)
    category = models.ForeignKey("Category",on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class User(models.Model):
    username = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.username


SEX_MAN = "Male"
SEX_WOMEN = "Women"
SEX_OTHER = "Other"

SEX_CHOICES = [(SEX_MAN, "Man"),
               (SEX_WOMEN, "Woman"),
               (SEX_OTHER, "Other"),
               ]


class Person(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name
