from django import forms
from .models import Profile, Workout, Goal

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [ 'age', 'height', 'weight', 'gender']

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['date', 'exercise', 'duration', 'distance', 'notes']

class Goals(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['target_weight', 'target_date', 'target_purpose' ]
