from django.urls import path

from . import views

app_name = "gamelogic"

urlpatterns = [
    path("astromancies", views.astromancies_view, name="astromancies"),
    path("artifacts", views.artifacts_view, name="artifacts"),
    path("psionics", views.psionics_view, name="psionics"),
]
