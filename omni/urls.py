from django.urls import path
from .views import EventList

urlpatterns = [
    path('', EventList.as_view(), name="homepage"),
    path('events/', EventList.as_view(), name="event_list"),
]
