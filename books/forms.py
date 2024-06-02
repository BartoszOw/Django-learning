from django import forms
from .models import Borrow, Comment

class ReturnBookForm(forms.ModelForm):
    class Meta:
        model = Borrow
        fields = ['borrow_date']
        widgets = {
            'is_returned': forms.HiddenInput()
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'content']