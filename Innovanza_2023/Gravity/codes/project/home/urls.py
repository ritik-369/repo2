from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path("", views.index),
    path("search_page", views.search_page),
    path("store", include("store.urls")),
]
