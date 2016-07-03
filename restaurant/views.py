from django.shortcuts import render
from django.http import HttpResponse
from restaurant.models import Restaurant

# Create your views here.

def sayHello(request):
	a  = Restaurant.objects.all()
	return render(request,"index.html", {'res' : a})


def fetch_restaurant(request,slug):
	a = Restaurant.objects.get(name_slug = slug)
	return render(request,"restaurant.html", {'res' : a})