from django.urls import path

from . import views
from .views import detallesComic

urlpatterns = [    
    path('catalogo/', views.catalogo, name= "catalogo"),
    path('home/', views.home, name= "home"),
    path('comic/<int:id>/', detallesComic, name='detallesComic'),
]