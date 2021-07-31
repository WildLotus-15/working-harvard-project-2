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
    path('<int:listing_id>/closing', views.closeListing, name="close_listing"),
    path('watchlist/<int:listing_id>/change/<str:reverse_method>', views.change_watchlist, name="change_watchlist"),
    path('watchlist/', views.watchlist, name="watchlist"),
]
