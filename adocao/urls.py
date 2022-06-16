from django.urls import path

from .views import AdocaoList

urlpatterns = [
    path("", AdocaoList.as_view()),
]