from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields import URLField, related


class User(AbstractUser):
    pass

class Category(models.Model):
    category = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.category}"

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(null=True)
    image_url = URLField(max_length=255, blank=True)
    starting_bid = models.FloatField(null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    current_bid = models.FloatField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    active = models.BooleanField(default=True)
    buyer = models.ForeignKey(User, on_delete=models.PROTECT, related_name='buyer', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    watchers = models.ManyToManyField(User, blank=True, related_name="watched_listings")

    def __str__(self):
        return f"{self.title}: {self.description}"

class Bid(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    offer = models.DecimalField(decimal_places=2, max_digits=5)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.author} -> ${self.offer}"

class Comment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")
    comment = models.CharField(max_length=155)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.comment}"