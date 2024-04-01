from django import forms
from gamelogic.backgrounds import backgrounds
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout


class BackgroundForm(forms.Form):
    choices = [(b, b) for b in backgrounds]
    background = forms.ChoiceField(choices=choices)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"

        self.helper.form_action = "chargen:generate_with_background"

        self.helper.add_input(
            Submit(
                "submit",
                "Generate",
                css_class="m-1 btn-secondary",
            )
        )
