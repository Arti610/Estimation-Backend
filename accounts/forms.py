from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm
from django.contrib.auth import get_user_model
from django import forms
from django.core import validators

from .models import CustomUser

CustomUser = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('first_name','last_name','email','phone_number','address','profile_image','user_type')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        validators.validate_email(email)

        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email  


class UpdateUserForm(forms.ModelForm):
    class Meta():
        model = CustomUser
        fields = ('first_name','last_name','email','phone_number','address','profile_image','user_type')


class CustomUserChangeForm(UserChangeForm): 
    class Meta:
        model = CustomUser
        fields = ('email',)


class CustomPasswordResetForm(PasswordResetForm):
    class meta:
        model = CustomUser
        fields = ('email',)