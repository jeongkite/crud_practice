from django.urls import path
from . import views

app_name = "bookmark"

urlpatterns = [
    path('', views.list, name='list')
]
