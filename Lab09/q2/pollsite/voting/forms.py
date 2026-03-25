from django import forms


class VoteForm(forms.Form):
    choice = forms.ChoiceField(
        label="How is the book ASP.NET with c# by Vipul Prakashan?",
        choices=[
            ("good", "Good"),
            ("satisfactory", "Satisfactory"),
            ("bad", "Bad"),
        ],
        widget=forms.RadioSelect,
    )
