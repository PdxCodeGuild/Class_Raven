from django import forms

class RenewKeyForm(forms.Form):
    #Form for admin to renew keys.
    renewal_date = forms.DateField(
            help_text="Enter new due back date")

   # widget = forms.DateInput()