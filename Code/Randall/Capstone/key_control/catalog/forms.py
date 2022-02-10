from django import forms

class RenewKeyForm(forms.Form):
    #Form for admin to renew keys.
    due_date = forms.DateField(
            help_text="Enter key return date.")

   # widget = forms.DateInput()