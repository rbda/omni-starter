from django.contrib import admin
from .models import Bet, Event, Outcome, Player, Team
from django import forms


class OutcomeAdminForm(forms.ModelForm):

    def clean_winner(self):
        if self.cleaned_data["winner"] is None:
            raise forms.ValidationError("team cannot be none", code="invalid_team_none")
        # if self.cleaned_data["winner"].id == self.instance.event.id:
        # print(f"winner.id: {self.cleaned_data['winner'].id}")
        event = self.data["event"]
        event_obj = Event.objects.get(id=event)
        # print(f"event.id: {event}")
        # print(f"event_obj: {event_obj}")
        # print(f"event_obj.teams: {event_obj.teams.all()}")
        if self.cleaned_data["winner"] not in event_obj.teams.all():
            raise forms.ValidationError("team not in event", code="invalid_event_team")
        return self.cleaned_data["winner"]

    def clean_loser(self):
        if self.cleaned_data["loser"] is None:
            raise forms.ValidationError("team cannot be none", code="invalid_team_none")
        event = self.data["event"]
        event_obj = Event.objects.get(id=event)
        if self.cleaned_data["loser"] not in event_obj.teams.all():
            raise forms.ValidationError("team not in event", code="invalid_event_team")
        return self.cleaned_data["loser"]

    def clean(self):
        super(OutcomeAdminForm, self).clean()

        if self.cleaned_data.get("winner") is None:
            raise forms.ValidationError("team cannot be none", code="invalid_team_none")
        if self.cleaned_data.get("loser") is None:
            raise forms.ValidationError("team cannot be none", code="invalid_team_none")
        if self.cleaned_data["winner"] == self.cleaned_data["loser"]:
            raise forms.ValidationError("winner and loser cannot be the same team", code="invalid_event_outcome")
        return self.cleaned_data


class BetAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Bet._meta.fields if field.name != ""]


class EventAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Event._meta.fields if field.name != ""]


class OutcomeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Outcome._meta.fields if field.name != ""]
    form = OutcomeAdminForm

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if db_field.name == "event":
            kwargs["queryset"] = db_field.related_model.objects.filter(outcome=None)
        return super(OutcomeAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


class PlayerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Player._meta.fields if field.name != ""]


class TeamAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Team._meta.fields if field.name != ""]


admin.site.register(Bet, BetAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Outcome, OutcomeAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Team, TeamAdmin)
