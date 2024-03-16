from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [  
  path('admin/',      admin.site.urls),
  path('', views.index),
  path('inicio/', include('onetoone.urls')),
  path('inicio/', include('onetomany.urls')),
  path('inicio/', include('manytomany.urls')),
]