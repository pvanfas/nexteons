from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ("timestamp",)
        widgets = {
            "name": forms.TextInput(attrs={"class": "ps-0 border-radius-0px border-color-extra-medium-gray bg-transparent form-control required", "placeholder": "Name"}),
            "email": forms.EmailInput(attrs={"class": "ps-0 border-radius-0px border-color-extra-medium-gray bg-transparent form-control required", "placeholder": "Email"}),
            "phone": forms.TextInput(attrs={"class": "ps-0 border-radius-0px border-color-extra-medium-gray bg-transparent form-control required", "placeholder": "Phone"}),
            "subject": forms.TextInput(attrs={"class": "ps-0 border-radius-0px border-color-extra-medium-gray bg-transparent form-control required", "placeholder": "Subject"}),
            "message": forms.Textarea(
                attrs={"class": "ps-0 border-radius-0px border-color-extra-medium-gray bg-transparent form-control required", "placeholder": "Message", "rows": "4"}
            ),
        }
