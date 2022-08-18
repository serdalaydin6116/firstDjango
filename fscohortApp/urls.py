from django.urls import path

from .views import fshome

urlpatterns = [

    path('fs', fshome),
]