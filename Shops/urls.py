from django.urls import path
from .views import home, register_shop, search_shops_view

urlpatterns = [
    path('', home, name='home'),  # Home page
    path('register/', register_shop, name='register_shop'),  # Registration page
    path('search/', search_shops_view, name='search_shops'),  # Search shops page
]