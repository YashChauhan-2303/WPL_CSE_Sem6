from django import forms


class FeedbackForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    gender = forms.ChoiceField(
        label='Gender',
        choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
        widget=forms.RadioSelect,
    )
    email = forms.EmailField(label='Email')
    comments = forms.CharField(label='Comments', widget=forms.Textarea(attrs={'rows': 3}))
    course = forms.ChoiceField(
        label='Course',
        choices=[
            ('ASP-XML', 'ASP-XML'),
            ('DotNET', 'DotNET'),
            ('JavaPro', 'JavaPro'),
            ('Unix,C,C++', 'Unix,C,C++'),
        ],
        widget=forms.Select,
    )
    technical_coverage = forms.ChoiceField(
        label='Technical Coverage',
        choices=[('Good', 'Good'), ('Bad', 'Bad'), ('Avg', 'Avg')],
        widget=forms.RadioSelect,
    )
