import enum

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProf(AbstractUser):
    username = models.CharField(max_length=300, unique=True, null=True)
    password = models.CharField(max_length=300)
    role = models.CharField(max_length=10, choices=[('SuperAdmin', 'SuperAdmin'), ('Guest', 'Guest')])
    image = models.ImageField(null=True, upload_to='imgs/', blank=True)


class BookJournal(models.Model):
    name = models.CharField(max_length=300)
    price = models.FloatField()
    description = models.TextField()
    created_at = models.DateTimeField()

    class Meta:
        abstract = True


class Book(BookJournal):
    num_pages = models.IntegerField()
    genre = models.TextField()


class Journal(BookJournal):
    type = models.CharField(max_length=6, choices=[('Bullet', 'Bullet'), ('Food', 'Food'), ('Travel', 'Travel'),
                                                   ('Sport', 'Sport')])
    publisher = models.CharField(max_length=300)



