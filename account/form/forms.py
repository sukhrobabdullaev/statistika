from ..models import Account
from django import forms
from django.core.exceptions import ValidationError


class AccountForm(forms.Form):
    password=forms.CharField(max_length=50,widget=forms.PasswordInput)
    password3=forms.CharField(max_length=50,widget=forms.PasswordInput )
    email=forms.EmailField(widget=forms.EmailInput)
    username=forms.CharField(max_length=50,widget=forms.TextInput)

    def clean_username(self):
        username=self.cleaned_data['username']
        r=Account.objects.filter(username=username)
        print('username',username)
        if r.count():
            raise ValidationError('Username Already exist')
        return username
    
    def clean_email(self):
        email=self.cleaned_data['email']
        r=Account.objects.filter(email=email)
        print('email',email)
        if r.count():
            raise ValidationError('Email Already exist')
        return email
    
    def clean_password(self):
        cleaned_data= super(AccountForm,self).clean()
        password=cleaned_data.get('password')
        password3=cleaned_data.get('password3')
        print('---paswordlar-->',password,password3)
        if password != password3:
            raise forms.ValidationError('Password and ComfirmPassword aren\'t same between them ') 
    
    def save(self,commit=True):
        user=Account.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            email=self.cleaned_data['email'],)
        print('useer',user)
        return user





    