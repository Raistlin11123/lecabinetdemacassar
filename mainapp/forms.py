from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="", max_length=30, widget= forms.TextInput(attrs={'class': "form-control"}))
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={'class': "form-control"}))
    subject = forms.CharField(label="", widget= forms.TextInput(attrs={'class': "form-control"}))
    content = forms.CharField(label="", widget=forms.Textarea(attrs={'class': "form-control form-control-comment"}))
