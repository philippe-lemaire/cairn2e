from django.shortcuts import render
from .character import Character
from .forms import BackgroundForm

# Create your views here.


def generate_character(request, background=None):
    return render(
        request,
        template_name="chargen/generate_character.html",
        context={"char": Character(background)},
    )


def generate_with_background(request):
    form = BackgroundForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            background = form.cleaned_data["background"]
            return generate_character(request, background)
    return render(
        request,
        template_name="chargen/generate_with_background.html",
        context={"form": form},
    )
