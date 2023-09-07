from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from user.models import User


class SignupForm(UserCreationForm):
    """
    This form will register user.
    """

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password1', 'password2', 'gender',
                  'profile_image']


class LoginForm(AuthenticationForm):
    """
    This form will authenticate user.
    """

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-lg'


class ProfileForm(forms.ModelForm):
    """
    This form is used to show profile of user.
    """

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'gender', 'profile_image', 'phone_number']
