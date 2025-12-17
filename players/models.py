from django.db import models

# Create your models here.


class Player(models.Model):
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    age = models.IntegerField()
    username = models.CharField(max_length=64, unique=True)


class Quest(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    difficulty = models.CharField(max_length=20)
    initiated = models.BooleanField(default=False)
    timer = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)
    player = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name='quests')
