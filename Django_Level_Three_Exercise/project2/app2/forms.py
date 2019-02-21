from django import forms
from app2.models import User

class NewUserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'
