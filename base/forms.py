from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from .models import User


class MyUserCreationForm(UserCreationForm):
    phone_num = PhoneNumberField(widget=PhoneNumberPrefixWidget)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'phone_num']
