from django.urls import path

from . import views

urlpatterns = [
    # your other URLs
    path("", views.chat, name="chat"),
]
