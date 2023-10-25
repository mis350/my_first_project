from django.urls import path
from helloworld.views import hello_view

urlpatterns = [
    path('hi/', hello_view),
]