from django import forms
from .models import Mailing


class MailingListForm(forms.ModelForm):
    """
    Create a form for the mailing model
    """
    class Meta:
        """
        Display the required fields
        """
        model = Mailing
        fields = "__all__"

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        """
        Add Placeholder to form fields
        """
        placeholders = {
            'first_name': 'First Name',
            'email': 'Email Address',
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
            # add class to fields
            self.fields[field].widget.attrs['class'] = 'my-2'
