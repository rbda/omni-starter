from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth import get_user_model
from django.views.generic.base import View

from .models import Event


class SignUpForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username",)


class SignUp(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'omni/signup.html'

    class SignUpForm(UserCreationForm):
        class Meta:
            model = get_user_model()
            fields = ("username",)
            # field_classes = {'username': UsernameField}


class EventList(LoginRequiredMixin, ListView):
    model = Event
