from django import forms
from .models import Contact

# Create your forms here.


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['email', 'last_name', 'first_name', 'message', ]

        def clean_email(self):
            email = self.cleaned_data.get('email')

            return email

