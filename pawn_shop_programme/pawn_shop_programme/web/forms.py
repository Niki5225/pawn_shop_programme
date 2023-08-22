from django import forms

from pawn_shop_programme.web.models import EuroBought, EuroSold, OtherSold, OtherBought, PoundSold, PoundBought

class BuyEuroForm(forms.ModelForm):
    class Meta:
        model = EuroBought
        fields = '__all__'

        labels = {
            'course_bought': 'Курс на купуване',
            'quantity': 'Количество',
        }

        widgets = {
            'course_bought': forms.TextInput(attrs={'placeholder': 'Напиши тук курса'}),
            'quantity': forms.TextInput(attrs={'placeholder': 'Напиши тук количеството'}),
        }


class SellEuroForm(forms.ModelForm):
    class Meta:
        model = EuroSold
        fields = '__all__'

        labels = {
            'course_sold': 'Курс на продаване',
            'quantity': 'Количество',
        }

        widgets = {
            'course_sold': forms.TextInput(attrs={'placeholder': 'Напиши тук курса'}),
            'quantity': forms.TextInput(attrs={'placeholder': 'Напиши тук количеството'}),
        }


class BuyPoundForm(forms.ModelForm):
    class Meta:
        model = PoundBought
        fields = '__all__'

        labels = {
            'course_bought': 'Курс на купуване',
            'quantity': 'Количество',
        }

        widgets = {
            'course_bought': forms.TextInput(attrs={'placeholder': 'Напиши тук курса'}),
            'quantity': forms.TextInput(attrs={'placeholder': 'Напиши тук количеството'}),
        }


class SellPoundForm(forms.ModelForm):
    class Meta:
        model = PoundSold
        fields = '__all__'

        labels = {
            'course_sold': 'Курс на продаване',
            'quantity': 'Количество',
        }

        widgets = {
            'course_sold': forms.TextInput(attrs={'placeholder': 'Напиши тук курса'}),
            'quantity': forms.TextInput(attrs={'placeholder': 'Напиши тук количеството'}),
        }


class BuyOtherValueForm(forms.ModelForm):
    class Meta:
        model = OtherBought
        fields = '__all__'

        labels = {
            'value_name': 'Име на валутата',
            'course_bought': 'Курс на купуване',
            'quantity': 'Количество',
        }

        widgets = {
            'course_bought': forms.TextInput(attrs={'placeholder': 'Напиши тук курса'}),
            'quantity': forms.TextInput(attrs={'placeholder': 'Напиши тук количеството'}),
        }


class SellOtherValueForm(forms.ModelForm):
    class Meta:
        model = OtherSold
        fields = '__all__'

        labels = {
            'course_sold': 'Курс на продаване',
            'quantity': 'Количество',
        }

        widgets = {
            'course_sold': forms.TextInput(attrs={'placeholder': 'Напиши тук курса'}),
            'quantity': forms.TextInput(attrs={'placeholder': 'Напиши тук количеството'}),
        }
