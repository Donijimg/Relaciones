from django.urls import path
from . import views

urlpatterns = [

    # path('nuevo/',views.nuevo,name="nuevo"),
    path('listado',views.listado,name="listado"),
    path('storage/<str:first_name>',views.storage,name="storage"),
    path('consultar/<int:id>',views.consultar,name="consultar"),
    path('modificar/<str:first_name>/<int:id>',views.modificar,name="modificar"),
    path('eliminar/<int:id>',views.eliminar,name="eliminar"),

]
