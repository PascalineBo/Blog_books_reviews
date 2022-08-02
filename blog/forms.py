from django import forms
from . import models
from django.contrib.auth import get_user_model

class TicketForm(forms.ModelForm):
    edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Ticket
        fields = ['title','description','image',]

class DeleteTicketForm(forms.Form):
    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)

class TicketReviewForm(forms.ModelForm):
    """ticket = forms.ModelMultipleChoiceField(queryset=models.Ticket.objects.all())"""
    RATING_CHOICES = [
        (0, "Zero"), (1, "*"), (2, "**"), (3, "***"), (4, "****"), (5, "*****")
    ]
    rating = forms.ChoiceField(widget=forms.RadioSelect, choices=RATING_CHOICES)

    class Meta:
        model = models.Review
        fields = ['ticket','headline','rating',
                  'content','body']


User = get_user_model()


class UserFollowsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['follows']
