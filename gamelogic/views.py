from django.shortcuts import render
from .astromancies import astromancies
from .artifacts import artifacts
from .psionics import psionics

# Create your views here.


def astromancies_view(request):
    template_name = "gamelogic/d66_tables.html"
    context = {"table": astromancies, "h1": "Astromancies"}
    return render(request, template_name, context)


def artifacts_view(request):
    template_name = "gamelogic/d66_tables.html"
    context = {"table": artifacts, "h1": "Artifacts"}
    return render(request, template_name, context)


def psionics_view(request):
    template_name = "gamelogic/d66_tables.html"
    context = {"table": psionics, "h1": "Psionics"}
    return render(request, template_name, context)
