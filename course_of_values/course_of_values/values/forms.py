from django import forms

from course_of_values.values.models import Value


class GetPriceBuyingForm(forms.ModelForm):
    class Meta:
        fields = ('value_name', 'course_of_buying',)
        model = Value

        labels = {
            'value_name': 'Име на валутата',
            'course_of_buying': 'Курс на купуване',
        }

        widgets = {
            'value_name': forms.TextInput(attrs={'placeholder': 'Напишете тук името на валутата'}),
            'course_of_buying': forms.TextInput(attrs={'placeholder': 'Напишете тук курса на валутата при закупуване'}),
        }


class GetPriceSelling(forms.ModelForm):
    class Meta:
        fields = ('value_name', 'course_of_selling',)
        model = Value

        labels = {
            'value_name': 'Име на валутата',
            'course_of_selling': 'Курс на продаване',
        }

        widgets = {
            'value_name': forms.TextInput(attrs={'placeholder': 'Напишете тук името на валутата'}),
            'course_of_buying': forms.TextInput(attrs={'placeholder': 'Напишете тук курса на валутата при продаване'}),
        }
