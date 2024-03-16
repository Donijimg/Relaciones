from django.urls import path
from . import views

urlpatterns = [

    path('create/',views.create,name="create"),
    # path('',views.index,name=""),
    # path('consultar/<int:id>',views.consultar,name="consultar"),
    # path('modificar/<str:nombre_admin>/<str:nombre_user>/<int:id>',views.modificar,name="modificar"),
    # path('eliminar/<int:id>',views.eliminar,name="eliminar"),
    # path('consultas',views.consultas,name="consultas")
]