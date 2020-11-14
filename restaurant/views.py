from django.shortcuts import render
from django.http import JsonResponse
from .models import Restaurant
from .serializers import RestaurantSerializer

# Create your views here.
def index(request):
    rest_list = Restaurant.objects.order_by('-pub_date')
    context = {'rest_list': rest_list}
    return render(request, 'food/index.html', context)


# Rest api end point
def get_rest_list(request):
    """
    Returns Json list of all restaurants
    """
    if request.method == "GET":
        rest_list = Restaurant.objects.order_by('-pub_date')
        serializer = RestaurantSerializer(rest_list, many=True)
        return JsonResponse(serializer.data, safe=False)