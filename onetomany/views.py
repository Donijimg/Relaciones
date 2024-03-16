from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter,Article
from datetime import date
# from .models import

def nuevo(request):
    # repo=Reporter(first_name="Doncan", last_name="Jimenez", email="dogo5@exmaple.com")
    # art1=Article(headline="Django basico",pub_date=date(2024,4,3),reporter=repo)
    # art2=Article(headline="Django intermedio",pub_date=date(2024,5,3),reporter=repo)
    # art3=Article(headline="Django avanzado",pub_date=date(2024,5,3),reporter=repo)
    # repo.save()
    # art1.save()
    # art2.save()
    # art3.save()
    
    # return HttpResponse("guardado")

    repo = Reporter.objects.get(id = 6)
    query = repo.article_set.all()
    return render(request, 'index.html',{
        'repo':repo,
        'query':query,
    })
