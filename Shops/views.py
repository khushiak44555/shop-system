from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Shop
from .serializers import ShopSerializer

def home(request):
    return render(request, 'home.html')

def search_shops_view(request):
    if request.method == 'GET':
        latitude = request.GET.get('latitude')
        longitude = request.GET.get('longitude')

        if latitude and longitude:
            # Redirect to the API view with the query parameters
            return redirect(f'/api/shops/search/?latitude={latitude}&longitude={longitude}')
    
    # Renders the form to accept latitude and longitude
    return render(request, 'search_shops.html')


@api_view(['GET'])
def search_shops_api(request):
    latitude = request.query_params.get('latitude')
    longitude = request.query_params.get('longitude')

    if latitude and longitude:
        try:
            latitude = float(latitude)
            longitude = float(longitude)

            # Optional: Set a maximum distance to filter shops (in this example, it's set to 10 units)
            max_distance = 10.0

            # Find shops within the maximum distance
            shops = Shop.objects.all()
            filtered_shops = []

            for shop in shops:
                # Calculate the distance
                distance = ((latitude - shop.latitude) ** 2 + (longitude - shop.longitude) ** 2) ** 0.5

                # Check if the shop is within the maximum distance
                if distance <= max_distance:
                    filtered_shops.append(shop)

            # Render the shops in a user-friendly HTML template
            return render(request, 'search_results.html', {'shops': filtered_shops})

        except ValueError:
            return render(request, 'search_results.html', {'error': 'Invalid latitude or longitude'})

    return render(request, 'search_results.html', {'error': 'Latitude and longitude are required'})


def register_shop(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')

        # Create a new Shop instance
        try:
            latitude = float(latitude)
            longitude = float(longitude)
            shop = Shop(name=name, latitude=latitude, longitude=longitude)
            shop.save()
            return redirect('home')
        except ValueError:
            return render(request, 'register_shop.html', {'error': 'Invalid coordinates.'})
        except Exception as e:
            print(f"Error saving shop: {e}")
            return render(request, 'register_shop.html', {'error': 'Failed to register shop.'})

    return render(request, 'register_shop.html')
