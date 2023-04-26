from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
# Create your models here.


class Student(AbstractUser):

    first_name=models.CharField(max_length=60)
    last_name=models.CharField(max_length=60)
    hostel=models.BooleanField(default=False)
    phone=models.CharField(max_length=10)

    groups = models.ManyToManyField(
        Group,
        blank=True,
        related_name='students'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='students'
    )

