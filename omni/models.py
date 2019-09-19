from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=200)
    sport = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Game(models.Model):
    time = models.DateTimeField()
    team = models.ManyToManyField(Team)

    def __str__(self):
        return self.team



