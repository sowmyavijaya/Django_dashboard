from django.shortcuts import render
from django.http import JsonResponse
from dashboard.models import Order
from django.core import serializers

# Create your views here.

def dashboard_with_pivot (request):
    return render(request, 'dashboard_with_pivot.html',{})

#Once called, this function will render dashboard_with_pivot.html - It 
#will contain the pivot table and pivot charts components.

def pivot_data(request):
    dataset = Order.objects.all()
    data = serializers.serialize('json',dataset)
    return JsonResponse(data, self=False)

#method that sends the response with data to the pivot table on the 
#app's front-end.Let's call it pivot_data.



