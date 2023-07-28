from django.db import models
from apps.users.models import Teacher


class Subject(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)
    credits = models.IntegerField()

    def __str__(self):
        return self.name


class Spell(models.Model):
    name = models.CharField(max_length=100)
    incantation = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
