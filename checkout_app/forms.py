from django import forms
from checkout_app.models import Billing

class BillingForm(forms.ModelForm):
    class Meta:
        model = Billing
        fields = ['address', 'email', 'phone']
