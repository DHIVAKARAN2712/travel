from django import forms
from .models import TravelPlace  # Make sure you're importing the correct model
from .models import VisitSubmission
class PlaceForm(forms.ModelForm):
    class Meta:
        model = TravelPlace
        fields = ['title', 'location', 'description']
class VisitSubmissionForm(forms.ModelForm):
    class Meta:
        model = VisitSubmission
        fields = ['place', 'reason']