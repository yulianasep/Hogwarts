from django.db import models


class House(models.Model):
    name = models.CharField(max_length=50)
    mascot = models.CharField(max_length=50)
    head_of_house = models.CharField(max_length=50)
    house_ghost = models.CharField(max_length=50)
    founder = models.CharField(max_length=50)
    school = models.CharField(max_length=50)

    def __str__(self):
        return self.name
