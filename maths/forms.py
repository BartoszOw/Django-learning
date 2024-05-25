from django import forms
from maths.models import Result

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['value', 'error']

    def clean(self):
        cleaned_data = super().clean()
        value = cleaned_data.get('value')
        error = cleaned_data.get('error')

        if value and error:
            raise forms.ValidationError('Podaj tylko jedna z wartości')
        elif not (value or error):
            raise forms.ValidationError('Nie podano żadnej wartości')