from django.contrib import admin
from .models import Team, Bet, Event, Outcome, Player

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Event)
admin.site.register(Bet)
admin.site.register(Outcome)
