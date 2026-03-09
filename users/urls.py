from django.urls import path
from users.views import get_user, inicio, acerca_de, list_products,register

urlpatterns = [
    path('usuario/', get_user, name='user'),
    path('cliente/', inicio, name='inicio'),
    path('acerca_de/', acerca_de, name='acerca_de'),
    path('productos/', list_products, name='list_products'),
    path('register/', register, name='register'),
]