from django.urls import path

from .views import PetList

urlpatterns = [
    path("", PetList.as_view()),
]