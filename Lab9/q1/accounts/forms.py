from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(label='UserName', max_length=100, required=True)
    password = forms.CharField(
        label='Password',
        required=False,
        widget=forms.PasswordInput(render_value=True),
    )
    email = forms.EmailField(label='Email id', required=False)
    contact_number = forms.CharField(label='Contact Number', required=False, max_length=20)
