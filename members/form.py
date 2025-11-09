from django import forms
from .models import MeetingMinutes, OrganizationInvitation

class MinutesUploadForm(forms.ModelForm):
    """
    Form for uploading or editing meeting minutes.
    """
    class Meta:
        model = MeetingMinutes
        fields = ['document', 'notes']


class OrganizationInvitationForm(forms.ModelForm):
    class Meta:
        model = OrganizationInvitation
        fields = ['name', 'email', 'contact_person', 'phone', 'message']

