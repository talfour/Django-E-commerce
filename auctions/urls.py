from django.urls import path
from . import views

app_name= "auctions"

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("<int:pk>/", views.detail_view, name="detail"),
    path("new_auction", views.new_listing, name="new_listing"),
    path("<int:pk>/watch_listing", views.add_watch_listing, name="watch_listing"),
    path("<int:pk>/remove_watch_listing", views.delete_watch_listing, name="remove_watch_listing"),
    path("watch_list",views.list_watching_listings, name="watch_list"),
    path("<int:pk>/inactive_listing",views.mark_listing_as_inactive, name="inactive_listing"),
    path("results/", views.search_by_categories, name="search"),
    path("categories/", views.categories_list, name="categories"),
    path("search/<str:category>", views.categories_requested, name="categories_requested"),
]
