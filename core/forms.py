from django import forms
from .models import Profile, Snippet, User


class ProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['user'].disabled = True
        self.fields['user'].widget = forms.HiddenInput()
    class Meta:
        model = Profile
        fields = ['profile_image', 'bio']

    

class SnippetForm(forms.ModelForm):

    class Meta:
        model = Snippet
        fields = [
            'title',
            'code',
            'language',
            'public',
        ]
        

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', '')
        super(SnippetForm, self).__init__(*args, **kwargs)
        self.fields['created_by']=forms.ModelChoiceField(queryset=User.objects.filter(username=user))