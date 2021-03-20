from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'date_release',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'date_release': forms.NumberInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
