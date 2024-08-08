from django import forms
from .models import Profile, Workout

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [ 'age', 'height', 'weight', 'gender']

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['date', 'exercise', 'duration', 'distance', 'notes']
