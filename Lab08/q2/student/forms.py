from django import forms

SUBJECT_CHOICES = [
    ('', '-- Select Subject --'),
    ('Mathematics', 'Mathematics'),
    ('Physics', 'Physics'),
    ('Chemistry', 'Chemistry'),
    ('Biology', 'Biology'),
    ('Computer Science', 'Computer Science'),
    ('English', 'English'),
    ('History', 'History'),
    ('Geography', 'Geography'),
]

class StudentForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'id': 'name'})
    )
    roll = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'id': 'roll'})
    )
    subject = forms.ChoiceField(
        choices=SUBJECT_CHOICES,
        widget=forms.Select(attrs={'id': 'subject'})
    )
