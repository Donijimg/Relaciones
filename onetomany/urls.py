from django.urls import path
from . import views

urlpatterns = [

    path('nuevo/',views.nuevo,name="nuevo"),
]