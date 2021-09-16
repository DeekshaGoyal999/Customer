from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Customer

class SignUpForm(UserCreationForm):
    class Meta:
        # model= User
        # fields=['username', 'first_name', 'last_name', 'email', ]
        model= Customer
        fields=['user', 'name', 'gender', 'locality', 'city', 'zipcode', 'state', 'mobile' ]