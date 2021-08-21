from django import forms
from .models import Profile, Snippet, User


class ProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
    
    class Meta:
        model = Profile
        fields = ['profile_image', 'bio']

    