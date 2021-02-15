from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    #Name = forms.CharField(
    #    required=True,
    #    widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}))
    #Email_Address = forms.EmailField(
    #    required=True,
    #    widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    #Phone_Number = forms.IntegerField(
    #    required=False,
    #    widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone Number'}))
    #message = forms.CharField(
    #    required=True,
    #    widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Message', 'rows':5}))
    
    class Meta:
        model = Contact
        fields = ('Name','Email_Address','Phone_Number','message')
        widgets = {
            'Name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),
            'Email_Address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}),
            'Phone_Number': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone Number'}),
            'message': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Message', 'rows':5}),
        }
    


