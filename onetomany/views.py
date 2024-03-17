from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter,Article
from datetime import date
# from .models import

#def nuevo(request):
    # repo=Reporter(first_name="Doncan", last_name="Jimenez", email="dogo5@exmaple.com")
    # art1=Article(headline="Django basico",pub_date=date(2024,4,3),reporter=repo)
    # art2=Article(headline="Django intermedio",pub_date=date(2024,5,3),reporter=repo)
    # art3=Article(headline="Django avanzado",pub_date=date(2024,5,3),reporter=repo)
    # repo.save()
    # art1.save()
    # art2.save()
    # art3.save()
    
    # return HttpResponse("guardado")

#    repo = Reporter.objects.get(id = 6)
#    query = repo.article_set.all()
#    return render(request, 'index.html',{
#        'repo':repo,
#        'query':query,
#    })

def listado(request):
  reporter = Reporter.objects.all()
  article=Article.objects.all()
  for obj in reporter:
    print(obj.first_name)
  for obj in article:
    print(obj.headline)
  return HttpResponse ("lista de places")

def storage(email,first_name,id):
  reporter = Reporter(first_name=first_name, email=email)
  article= Article(id=id)
  reporter.save()
  article.save()
  return HttpResponse ("guardamos los datos")
  
def consultar(requets,id):
  reporter= Reporter.objects.get(id=id)
  article=Article.objects.all()
  return HttpResponse (f"nombre: {reporter.first_name}, addres:{reporter.email}, restaurant: {article}")


def modificar(request, first_name,id):
  reporter=Reporter.objects.get(id=id)
  reporter.first_name=first_name
  reporter.save()
  return HttpResponse("post actualizado")

def eliminar(request,id):
  reporter=Reporter.objects.get(id=id)
  reporter.delete()
  return HttpResponse("post eliminado")
