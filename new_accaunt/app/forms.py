from django import forms


class UserForm(forms.Form):
    firstname = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите ник',
        }),
        label="Имя"
    )

    email = forms.EmailField(
        required=True,
        widget = forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите почтовый адрес',
        }),
        label='Email'
    )


class AccauntUser(UserForm):

    ratting = forms.ChoiceField(
        choices=(
            (1, '1 звезда'),
            (2, '2 звезды'),
            (3, '3 звезды'),
            (4, '4 звезды'),
            (5, '5 звезды')
        ),
        widget=forms.Select(attrs={
            'class': 'form-select',
            'placeholder': 'Выберите рейтинг приложение',
        }),
        label='Рейтинг',
        initial=1
    )

    description = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите описание',
        }),
        label="Описание"
    )



class Book(UserForm):

    ratting = forms.CharField(
        max_length='100',
        required = True,
        widget = forms.NumberInput(attrs={
            'class':'form-control',
            'placeholder':'Оцените книгу от 1 до 100'
        }),
        label = 'Оценка'
    )

    description = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите описание',
        }),
        label="Описание"
    )
    spoiler = forms.BooleanField(
        required=False
    )
