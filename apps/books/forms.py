from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'})
        }
