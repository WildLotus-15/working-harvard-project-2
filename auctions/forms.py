from django.db.models.base import Model
from .models import Listing, Bid, Comment
from django.forms import ModelForm

class NewListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'starting_bid', 'image_url', 'category']

class NewBidForm(ModelForm):
    class Meta:
        model = Bid
        fields = ['offer']

    
class NewCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']