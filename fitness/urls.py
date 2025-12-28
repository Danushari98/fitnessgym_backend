from django.urls import path
from .views import enquire

urlpatterns = [
    path("enquire/", enquire),
]
