from django.contrib import admin
from django.urls import path, include
from . import views

app_name="index"

urlpatterns = [
    path('', views.index, name="index"),
    path('list/', views.list, name="list"),
    path('create/', views.create, name="create"),
    path('<int:notice_pk>/', views.detail, name="detail"),
    path('<int:notice_pk>/update/', views.update, name="update"),
    path('<int:notice_pk>/delete/', views.delete, name="delete"),

    # path('noticeboard/', include('noticeboard.urls')),
]