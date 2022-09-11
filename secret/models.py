from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField(max_length=255)
    manager = models.ForeignKey(User, on_delete=models.PROTECT, null=True)

class Folder(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500, null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    team = models.ForeignKey(Team, on_delete=models.PROTECT, null=True)

class Secret(models.Model):
    name = models.CharField(max_length=50)
    data = models.TextField()
    folder = models.ForeignKey(Folder, on_delete=models.PROTECT)
