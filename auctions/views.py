from typing import List
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import User, Listing, Bid
from .forms import NewBidForm, NewCommentForm, NewListingForm

def activeListing(request):
    listing = Listing.objects.filter(active=True)
    return render(request, "auctions/index.html", {
        "listing": listing
    })    

def listing(request, listing_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    listing = Listing.objects.get(pk=listing_id)
    return render(request, "auctions/listing.html", {
        "listing": listing,
        "comments": listing.comments.all(),
        "comment_form": NewCommentForm(),
        "bid_form": NewBidForm(),
        "bid": Bid.objects.all()
    })

def newListing(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    if request.method == "POST":
        form = NewListingForm(request.POST)
        if form.is_valid():
            print("printing Post:", request.POST)
            newListing = form.save(commit=False)
            newListing.author = request.user
            newListing.save()
            return HttpResponseRedirect(reverse("index"))
    return render(request, "auctions/new.html", {
        "form": NewListingForm(),
        "success": True
    })

def bid(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    bids = Bid.objects.filter(listing=listing)
    bid_count = bids.count()
    form = NewBidForm(request.POST)
    if form.is_valid():
        offer = float(request.POST['offer'])
        if is_valid(offer, listing):
            newBid = form.save(commit=False)
            listing.current_bid = offer
            newBid.listing = listing 
            newBid.author = request.user
            newBid.save()
            listing.save()
            return HttpResponseRedirect(reverse("bid", args=[listing_id]))
        else:
            return render(request, "auctions/bid.html", {
                "listing": listing,
                "form": NewBidForm(),
                "value_error": True,
                "bid_count": bid_count
            })
    else:
        return render(request, "auctions/bid.html", {
            "form": NewBidForm(),
            "listing": listing,
            "bid_count": bid_count
        })

def is_valid(offer, listing):
    if offer >= listing.starting_bid and (listing.current_bid is None or offer > listing.current_bid):
        return True
    else:
        return False    

def comment(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    form = NewCommentForm(request.POST)
    if form.is_valid():
        newComment = form.save(commit=False)
        newComment.listing = listing
        newComment.author = request.user
        newComment.save()
        return HttpResponseRedirect(reverse("listing", args=[listing_id]))

def closeListing(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    if request.user == listing.author:
        listing.active = False
        listing.buyer = Bid.objects.filter(listing=listing).last().user
        listing.save()

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
