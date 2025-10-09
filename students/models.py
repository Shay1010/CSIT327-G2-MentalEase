from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Student(AbstractUser):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.username

    groups = models.ManyToManyField(
        Group,
        related_name='student_users',  # Unique related_name to avoid clashes
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='student_users',  # Unique related_name to vavoid clashes
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.'
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]  # still needed by Django but login uses email
