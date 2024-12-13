from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, UsernameField
from django import forms
from .models import UserAccount

class UserAccountCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = UserAccount
        fields = ['username', 'password1', 'password2',  'name', 'is_organization', 'inn']

    username = forms.CharField(max_length=150, 
                               label='Логин',
                               help_text='Рекомендуется использовать ник из Телеграм',
                               required=True,
                               widget=forms.TextInput(attrs={'id': 'username'})
                               )
    password1 = forms.CharField(min_length=8, 
                                max_length=25, 
                                widget=forms.PasswordInput,
                                label='Пароль', 
                                help_text='Длина от 8 до 25 символов с минимум 1 заглавной буквой 1 строчной буквой и 1 цифрой',
                                required=True
                                )
    password2 = forms.CharField(min_length=8, 
                                max_length=25, 
                                label='Подтверждение пароля',
                                widget=forms.widgets.PasswordInput, 
                                help_text='Введите пароль еще раз',
                                required=True
                                )
    name = forms.CharField(max_length=150, 
                                label='Ваше ФИО',
                                help_text='Чтоб мы могли корретно к Вам обратиться',
                                required=False
                            )
    is_organization = forms.BooleanField(label='Регистрируюсь как организация: ',
                                required=False)
    
    inn = forms.CharField(max_length=10, 
                                label='ИНН',
                                required=False
                            )

class CustomAuthenticationForm(AuthenticationForm):
    class Meta(AuthenticationForm):
        model = UserAccount
        fields = ['username', 'password']

    username = UsernameField(
        label='Логин',
        widget=forms.TextInput(attrs={'autofocus': True})
    )

    password = forms.CharField(
        min_length=8,
        max_length=25,
        widget=forms.widgets.PasswordInput,
        label='Пароль'
    )


    

