from django.contrib import admin
from django.urls import path, include
from . import views

app_name="noticeboard"

urlpatterns = [
    path('', views.list, name="list"),
    # path('index/', include('index.urls')),
]