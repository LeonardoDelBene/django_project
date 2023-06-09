from django import forms
from .models import Workout

class WorkoutForm(forms.Form):
    year = forms.IntegerField(widget=forms.HiddenInput())
    month = forms.IntegerField(widget=forms.HiddenInput())
    day = forms.IntegerField(widget=forms.HiddenInput())
    workout = forms.ModelChoiceField(queryset=None)

    def __init__(self, user, *args, **kwargs):
        super(WorkoutForm, self).__init__(*args, **kwargs)
        self.fields['workout'].queryset = Workout.objects.filter(user=user)
