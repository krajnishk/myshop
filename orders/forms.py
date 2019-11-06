from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    """Form definition for OrderCreate."""

    class Meta:
        """Meta definition for OrderCreateform."""

        model = Order
        fields = ['first_name', 'last_name',
                  'email', 'address', 'postal_code', 'city']
