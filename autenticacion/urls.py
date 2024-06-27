from django.urls import path
from .views import VRegistro, close_session, logear

urlpatterns = [
    path('registro/', VRegistro.as_view(), name='registro'),
    path('logout/', close_session, name='logout'),
    path('login/', logear, name='login'),
]
