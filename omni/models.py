from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=200)
    sport = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Event(models.Model):
    time = models.DateTimeField()
    location = models.CharField(max_length=250)
    venue = models.CharField(max_length=250)
    teams = models.ManyToManyField(Team, related_name="event_team")

    def __str__(self):
        # teams_list = self.teams.all()
        # print(self.teams.all())
        return "{}: {} vs {}".format(self.time.date(), *self.teams.all())


class Player(models.Model):
    username = models.CharField(max_length=250)
    balance = models.DecimalField(decimal_places=2, max_digits=4)


class Outcome(models.Model):
    """
    the result of the event
    """
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="event")
    # print(dir(event))
    # print(event)
    winner = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="winner", blank=True, null=True)
    loser = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="loser", blank=True, null=True)

    def __str__(self):
        return str(self.event)


class Bet(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=4)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

#
# class Game(models.Model):
#     time = models.DateTimeField()
#     team = models.ManyToManyField(Team)
#
#     def __str__(self):
#         return str(self.team.all())
