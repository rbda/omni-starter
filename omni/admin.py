from django.contrib import admin
from .models import Bet, Event, Outcome, Player, Team


class BetAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Bet._meta.fields if field.name != ""]


class EventAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Event._meta.fields if field.name != ""]


class OutcomeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Outcome._meta.fields if field.name != ""]


class PlayerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Player._meta.fields if field.name != ""]


class TeamAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Team._meta.fields if field.name != ""]


admin.site.register(Bet, BetAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Outcome, OutcomeAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Team, TeamAdmin)