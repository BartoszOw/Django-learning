from django import forms
from posts.models import Author

class PostForm(forms.Form):
    title = forms.CharField(required=True)
    content = forms.CharField(widget=forms.Textarea, required=True)
    author = forms.ModelChoiceField(queryset=Author.objects.all(), widget=forms.Select, required=True)

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')

        if not title or not content:
            raise forms.ValidationError('Nie ma uzupelnionych danych')
        
        return cleaned_data
    
class AuthorForm(forms.Form):
    nick = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    author_bio = forms.CharField(widget=forms.Textarea, required=False)

    def clean(self):
        cleaned_data = super().clean()
        nick = cleaned_data.get('nick')
        email = cleaned_data.get('email')
        
        if not nick or not email:
            raise forms.ValidationError('Brakuje nicku lub maila')
        
        return cleaned_data