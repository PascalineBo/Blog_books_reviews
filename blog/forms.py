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
    edit_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)
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
    followed_user = forms.CharField(max_length=256,
                                    widget=forms.TextInput(attrs={"placeholder": " Nom d'utilisateur "}))

    class Meta:
        model = models.UserFollows
        fields = ['followed_user']

    def clean(self):
        cleaned_data = super(UserFollowsForm, self).clean()
        followed_user = cleaned_data.get('followed_user')
        if models.UserFollows.objects.filter(followed_user=followed_user).exists():
            raise forms.ValidationError('Category already exists')
