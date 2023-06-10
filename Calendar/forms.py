from django import forms
from .models import Workout

from django import forms
from django.contrib.admin.widgets import AdminDateWidget

class WorkoutForm(forms.Form):
    workout = forms.ModelChoiceField(queryset=Workout.objects.none())
    year = forms.IntegerField()
    month = forms.IntegerField()
    day = forms.IntegerField()

    def __init__(self, user, *args, **kwargs):
        super(WorkoutForm, self).__init__(*args, **kwargs)
        self.fields['workout'].queryset = Workout.objects.filter(user=user)
        self.fields['workout'].label_from_instance = lambda obj: obj.name
