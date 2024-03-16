from django.shortcuts import render
from django.http import HttpResponse
from .models import Article,Publication
from datetime import date
# from .models import

def articulos(request):
  art1=Article(headline="Articlo 1")
  art2=Article(headline="Articlo 2")
  art3=Article(headline="Articlo 3")

  art1.save()
  art2.save()
  art3.save()

  pub1=Publication(title="titulo 1")
  pub2=Publication(title="titulo 2")
  pub3=Publication(title="titulo 3")
  pub4=Publication(title="titulo 4")
  pub5=Publication(title="titulo 5")
  pub6=Publication(title="titulo 6")
  pub7=Publication(title="titulo 7")
  pub8=Publication(title="titulo 8")

  pub1.save()
  pub2.save()
  pub3.save()
  pub4.save()
  pub5.save()
  pub6.save()
  pub7.save()
  pub8.save()

  art1.publications.add(pub1)
  art1.publications.add(pub2)
  art1.publications.add(pub3)

  art2.publications.add(pub4)
  art2.publications.add(pub5)
  art2.publications.add(pub6)

  art3.publications.add(pub7)
  art3.publications.add(pub8)

  return HttpResponse("articulos")