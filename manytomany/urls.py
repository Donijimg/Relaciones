from django.urls import path
from . import views

urlpatterns = [

    # path('articulos/',views.articulos,name="articulos"),
    path('listado',views.listado,name="listado"),
    path('storage/<str:title>',views.storage,name="storage"),
    path('consultar/<int:id>',views.consultar,name="consultar"),
    path('modificar/<str:title>/<int:id>',views.modificar,name="modificar"),
    path('eliminar/<int:id>',views.eliminar,name="eliminar"),
]