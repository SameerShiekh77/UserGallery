from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import User
class SignUpForm(UserCreationForm,forms.ModelForm):
    username = forms.CharField(label='Username', max_length=30, required=True, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.',widget=forms.TextInput(attrs={'class': 'border border-gray-400 py-2 px-3 rounded-lg w-full'}))
    email = forms.EmailField(label='Email', max_length=254, required=True, help_text='Required. Inform a valid email address.',widget=forms.TextInput(attrs={'class': 'border border-gray-400 py-2 px-3 rounded-lg w-full'}))
    password1 = forms.CharField(label='Password', max_length=30, required=True, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.',widget=forms.PasswordInput(attrs={'class': 'border border-gray-400 py-2 px-3 rounded-lg w-full'}))
    password2 = forms.CharField(label='Password confirmation', max_length=30, required=True, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.',widget=forms.PasswordInput(attrs={'class': 'border border-gray-400 py-2 px-3 rounded-lg w-full'}))
    phone_number = forms.CharField(label='Phone', max_length=30, required=True, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.',widget=forms.TextInput(attrs={'class': 'border border-gray-400 py-2 px-3 rounded-lg w-full'}))
    country = forms.CharField(label='Country', max_length=30, required=True, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.',widget=forms.TextInput(attrs={'class': 'border border-gray-400 py-2 px-3 rounded-lg w-full'}))
    first_name = forms.CharField(label='Username', max_length=30, required=True, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.',widget=forms.TextInput(attrs={'class': 'border border-gray-400 py-2 px-3 rounded-lg w-full'}))
    last_name = forms.CharField(label='Username', max_length=30, required=True, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.',widget=forms.TextInput(attrs={'class': 'border border-gray-400 py-2 px-3 rounded-lg w-full'}))
    
    class Meta:
        model = User
        fields = ('profile_image','username', 'email', 'password1', 'password2','country','phone_number','first_name','last_name')
        extra_kwargs = {'password1': {'write_only': True}, 'password2': {'write_only': True}, 'email':{'unique':True}}