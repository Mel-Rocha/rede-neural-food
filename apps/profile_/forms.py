from django import forms

from apps.profile_.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'age', 'weight', 'height', 'illness', 'intolerance', 'goal', 'diet', 'gender']