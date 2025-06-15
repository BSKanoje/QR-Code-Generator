from django import forms

class QRCodeForm(forms.Form):
    title = forms.CharField(
        max_length=50, 
        label='Title', 
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Name of restaurant, event, business, etc.',
        })
        )
    url = forms.URLField(
        max_length=200, 
        label='URL / Website Link',
        widget=forms.URLInput(attrs={
            'class': 'form-control',
            'placeholder': 'Link to menu, brochure, portfolio, resume, booking page, etc.',
        })
        )