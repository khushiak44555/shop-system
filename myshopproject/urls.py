from django.urls import path
from django.contrib import admin
from Shops.views import home, register_shop, search_shops_api, search_shops_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('register-shop/', register_shop, name='register_shop'),
    path('shops/search/', search_shops_view, name='search_shops_api'),  # HTML form for searching shops
    path('api/shops/search/', search_shops_api, name='search_shops'),  # API endpoint for searching shops
]
