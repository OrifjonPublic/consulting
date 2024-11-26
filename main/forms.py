from django import forms
from .models import ( Activity, ActivityPhotos, Company, 
                     Contact, FAQ, Hamkorlar, Logo, HeroTitle,
                     Reviews, SocialMedia, Takliflar, Team, User, Videourl
                    )

class TakliflarForm(forms.ModelForm):
    class Meta:
        model = Takliflar
        fields = ['full_name', 'phone_number', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'full_name': 'Ism/Familiya',
            'phone_number': 'Telefon raqam',
            'message': 'Xabar',
        }
        