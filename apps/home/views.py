from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "home/index.html" )


def menu(request):
    return render(request, "home/menu.html" )


def blog(request):
    return render(request, "home/blog.html" )


def listas(request):
    mi_lista = [-11, 20, 3, 41]
    otra_lista = ["hola", "como", "estas", "?"]
    mi_lista_1 =  ["cadena", 1000,  12.34, 0, "otra cadena"]

    return render(request, "home/listas.html", mi_lista)