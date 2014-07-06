# apps.linkengine.forms
from django import forms
from models import UserProfile, Link


# use generic model to start User Profile
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ("user",)


# use generic form for links
class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        exclude = ("submitter", "rank_score")