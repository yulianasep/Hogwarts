from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

from apps.houses.models import House


class CustomUser(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    groups = models.ManyToManyField(
        'auth.Group',
        related_name='auth_user_set',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='auth_user_set',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )
    

    def __str__(self):
        return self.username
    

class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Profesor: {self.user.username}"


class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return f"Estudiante: {self.user.username}"