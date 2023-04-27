from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
# Create your models here.


class Warden(AbstractUser):

    first_name=models.CharField(max_length=60)
    last_name=models.CharField(max_length=60)
    phone=models.CharField(max_length=10)

    groups = models.ManyToManyField(
        Group,
        blank=True,
        related_name='wardens'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='wardens'
    )
