from django import forms

class FormName(forms.Form):
    name = forms.CharField( max_length=255, required=False)
    email=forms.EmailField( required=False)
    text = forms.CharField( max_length=255, required=False, widget=forms.Textarea)
