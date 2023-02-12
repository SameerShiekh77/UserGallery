from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import User
class SignUpForm(UserCreationForm,forms.ModelForm):
    username = forms.CharField(label='Username', max_length=30, required=True, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.',widget=forms.TextInput(attrs={'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer'}))
    email = forms.EmailField(label='Email', max_length=254, required=True, help_text='Required. Inform a valid email address.',widget=forms.TextInput(attrs={'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer'}))
    password1 = forms.CharField(label='Password', max_length=30, required=True, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.',widget=forms.PasswordInput(attrs={'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer'}))
    password2 = forms.CharField(label='Password confirmation', max_length=30, required=True, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.',widget=forms.PasswordInput(attrs={'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer'}))
    phone = forms.CharField(label='Phone', max_length=30, required=True, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.',widget=forms.TextInput(attrs={'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer'}))
    country = forms.CharField(label='Country', max_length=30, required=True, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.',widget=forms.TextInput(attrs={'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer'}))
    first_name = forms.CharField(label='Username', max_length=30, required=True, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.',widget=forms.TextInput(attrs={'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer'}))
    last_name = forms.CharField(label='Username', max_length=30, required=True, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.',widget=forms.TextInput(attrs={'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2','country','phone','first_name','last_name')
        extra_kwargs = {'password1': {'write_only': True}, 'password2': {'write_only': True}}

    # def clean_password2(self):
    #     password = self.cleaned_data.get("password")
    #     password2 = self.cleaned_data.get("password2")
    #     if password != password2:
    #         raise forms.ValidationError("Passwords do not match")
    #     return password

   
