from django.db.models.base import Model
from .models import Listing, Bid, Comment
from django.forms import ModelForm, widgets
from django import forms

class NewListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'starting_bid', 'image_url', 'category']

class NewBidForm(ModelForm):
    def __init__(self, *args, **kwargs):
            super(NewBidForm, self).__init__(*args, **kwargs)
            self.fields['offer'].widget.attrs = {'class': 'form-control', 'placeholder': 'Enter an offer...' }
            self.fields['offer'].label = ''
    
    class Meta:
        model = Bid
        fields = ['offer']

    
class NewCommentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(NewCommentForm, self).__init__(*args, **kwargs)
        self.fields['comment'].widget.attrs = {'class':'form-control', 'placeholder': 'Write a comment...',}
        self.fields['comment'].label = ''

    class Meta:
        model = Comment
        fields = ['comment']