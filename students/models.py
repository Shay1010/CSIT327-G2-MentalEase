from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Student(AbstractUser):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    year_program = models.CharField(max_length=100, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.username

    groups = models.ManyToManyField(
        Group,
        related_name='student_users',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='student_users',
        blank=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
