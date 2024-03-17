from django.shortcuts import render
from django.http import HttpResponse
from .models import Place,Restaurant

# def create(request):
  # place = Place(name="doncan", addres="calle 123")
  # restaurant = Restaurant(place = place, employees = 5)
  # place.save()
  # restaurant.save()
  # return HttpResponse ("datos creados")


  # restaurante=Restaurant.objects.get(place_id=8)
  # print(restaurante.place.addres)
  # return HttpResponse (restaurante.place.addres)

def listado(request):
  places = Place.objects.all()
  restaurants=Restaurant.objects.all()
  for obj in places:
    print(obj.name)
  for obj in restaurants:
    print(obj.place)
  return HttpResponse ("lista de places")

def storage(addres,name,id):
  places = Place(name=name, addres=addres)
  restaurants= Restaurant(id=id)
  restaurants.save()
  places.save()
  return HttpResponse ("guardamos los datos")
  
def consultar(requets,id):
  places= Place.objects.get(id=id)
  restaurants=Restaurant.objects.all()
  return HttpResponse (f"nombre: {places.name}, addres:{places.addres}, restaurant: {restaurants}")


def modificar(request, name,id):
  places=Place.objects.get(id=id)
  places.name=name
  places.save()
  return HttpResponse("post actualizado")

def eliminar(request,id):
  places=Place.objects.get(id=id)
  places.delete()
  return HttpResponse("post eliminado")
