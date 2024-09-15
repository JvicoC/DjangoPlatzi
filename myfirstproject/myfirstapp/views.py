from .models import Book, Car
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def my_view(request):
    car_list=[
        {"title":"BMW"},
        {"title":"Mazda"},
        {"title":"Toyota"},
    ]
    context={
        "car_list":car_list
    }
    return render(request, "myfirstapp/car_list.html", context)# necesita un request y un template, tambien se puede aumentar un contexto de tipo diccionario para

class CarListView(TemplateView):
    template_name="myfirstapp/car_list.html"

    def get_context_data(self):
        car_list=[
        {"title":"BMW"},
        {"title":"Mazda"},
        {"title":"Toyota"},
        ]
        return {
            "car_list":car_list
        }

class CarListView02(TemplateView):
    template_name="myfirstapp/car_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cars01'] = Car.objects.all().filter(title="Mazda")
        context['libros'] = Book.objects.all()
        return context

def my_view_test(request, *args, **kwargs):
    print(args)
    print(kwargs)
    return HttpResponse(" Hola desde views...!!!")