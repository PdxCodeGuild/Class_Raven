from django import forms
import datetime 
from django.core.exceptions import ValidationError



class RenewKeyForm(forms.Form):
    #Form for admin to renew keys.
    renewal_date = forms.DateField(help_text="Enter new due date.")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        """# Check if not in past.       #Add back later after testing
        if data < datetime.date.today():
            raise ValidationError(('Invalid date - renewal in past'))
        """    
        # Makes sure date doesn't exceed the allowed specified
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(('Error: Date entered exceeds 4 weeks, try again.'))

        # Remember to always return the cleaned data.
        return data