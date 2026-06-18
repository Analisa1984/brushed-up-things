from django import forms


class ContactForm(forms.Form):
    """ contact form for user inquiries"""
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)