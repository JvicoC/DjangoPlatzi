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