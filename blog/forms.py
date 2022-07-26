from django import forms
from django.contrib.auth import get_user_model
from . import models

class TicketForm(forms.ModelForm):
    edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Ticket
        fields = ['title','description','image',]

class DeleteTicketForm(forms.Form):
    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)

class TicketReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ['ticket','headline',
                  'rating','content','body']

User = get_user_model()


class FollowUsersForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['follows']
