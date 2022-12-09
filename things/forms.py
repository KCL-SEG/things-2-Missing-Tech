"""Forms of the project."""
from django import forms
from .models import Thing

# Create your forms here.
class ThingForm(forms.Form):
    """Form of the Thing model."""

    class Meta:
        """Meta class of the form."""
        model = Thing

    name = forms.CharField(widget=forms.TextInput)
    description = forms.CharField(widget=forms.Textarea)
    quantity = forms.CharField(widget=forms.NumberInput)