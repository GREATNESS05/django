from .models import Profile
from django import forms
class ProfileForm(forms.ModelForm):
    class meta:
        model = Profile
        fields = ['profileimg', 'location', 'bio']
        labels = {
            "profileimg" : "profile pic",
            "location" : "location",
            "bio" : "bio"
        }

        

       
