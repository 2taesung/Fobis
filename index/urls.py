from django.contrib import admin
from django.urls import path, include
from . import views

app_name="index"

urlpatterns = [
    path('', views.index, name="index"),
    path('list/', views.list, name="list"),
    path('<int:notice_pk>/detail/', views.detail, name="detail"),

    # path('noticeboard/', include('noticeboard.urls')),
]