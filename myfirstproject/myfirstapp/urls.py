"""
URL configuration for myfirstproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf (inlcuir otras URLS, agrupadas por aplicaciones)
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.http import HttpResponse
from django.urls import path
from .views import my_view, my_view_test, CarListView, CarListView02

urlpatterns = [
    #path("listado/",my_view),
    path("listado/",CarListView.as_view()),
    #path("cars/",CarListView02.as_view()),
    path('cars/', CarListView02.as_view()),
    path("detalle/<int:id>",my_view_test),
    #path("detalle/<int:id>",CarListView.as_view()),
    path("marcas/<str:brand>",my_view_test)    
]
