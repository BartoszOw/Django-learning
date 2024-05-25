from django import forms
from posts.models import Author, Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')

        if not title or not content:
            raise forms.ValidationError('Nie ma uzupelnionych danych')
        
        return cleaned_data
    
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        nick = cleaned_data.get('nick')
        email = cleaned_data.get('email')
        
        if not nick or not email:
            raise forms.ValidationError('Brakuje nicku lub maila')
        
        return cleaned_data