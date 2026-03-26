from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from users.models import Product
from .forms import RegisterForm

from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView


# Create your views here.
def get_user(request):
    return HttpResponse("Hello World")


def inicio(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, "base.html", context=context)


def acerca_de(request):
    return render(request, "acerca_de.html")


def list_products(request):
    products = Product.objects.all()
    return render(request, "products.html", context={"products": products})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()   # crea el usuario
            login(request, user) # inicia sesión automáticamente
            return redirect('inicio')  # lo manda a inicio

    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        user = self.request.user

        if user.is_superuser:
            return reverse_lazy('admin:index')

        if user.groups.filter(name__in=['Lector', 'Escritor', 'Editor']).exists():
            return reverse_lazy('article_list')

        return reverse_lazy('inicio')