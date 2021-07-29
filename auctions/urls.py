from django.urls import path

from . import views

urlpatterns = [
    path("", views.activeListing, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('new', views.newListing, name="new"),
    path('<int:listing_id>', views.listing, name="listing"),
    path('<int:listing_id>/bid', views.bid, name="bid"),
    path('<int:listing_id>/comment', views.comment, name="comment"),
]
