from django import forms
from .models import Users, UserManager
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password


class RegistForm(forms.ModelForm):
    username = forms.CharField(label='ユーザ名', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='メールアドレス', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(label='パスワード再入力', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta():
        model = Users
        fields = ('username', 'email', 'password')
        
    def clean_username(self):
        value = self.cleaned_data['username']
        if len(value) < 3:
            raise forms.ValidationError(
                '%(min_length)s文字以上で入力してください', params={'min_length': 3})
        return value

    def clean_email(self):
        value = self.cleaned_data['email']
        return value

    def clean_password(self):
        value = self.cleaned_data['password']
        return value
                
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']
        if password !=confirm_password:
            raise forms.ValidationError('パスワードが異なります')
        
    def save(self, commit=False):
        user = super().save(commit=False)
        validate_password(self.cleaned_data['password'], user)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user
    
class LoginForm(forms.Form):
    email = forms.EmailField(label="メールアドレス")
    password = forms.CharField(label="パスワード", widget=forms.PasswordInput())
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise ValidationError("メールアドレスを入力してください。")
        return email
    
class UserEditForm(forms.ModelForm):
    username = forms.CharField(label='ユーザ名')
    email = forms.EmailField(label='メールアドレス')
        
    class Meta:
        model = Users
        fields = ('username', 'email')
        
class PasswordChangeForm(forms.Form):
    
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='パスワード再入力', widget=forms.PasswordInput())
        
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']
        if password !=confirm_password:
            raise forms.ValidationError('パスワードが異なります')
        
    def save(self, user, commit=True):
        password = self.cleaned_data["password"]
        user.set_password(password)  # パスワードのハッシュ化
        if commit:
            user.save()
        return user