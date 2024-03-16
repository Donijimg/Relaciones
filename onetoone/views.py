from django.shortcuts import render
from django.http import HttpResponse
from .models import Place,Restaurant

def create(request):
  # place = Place(name="doncan", addres="calle 123")
  # restaurant = Restaurant(place = place, employees = 5)
  # place.save()
  # restaurant.save()
  # return HttpResponse ("datos creados")


  restaurante=Restaurant.objects.get(place_id=8)
  print(restaurante.place.addres)
  return HttpResponse (restaurante.place.addres)