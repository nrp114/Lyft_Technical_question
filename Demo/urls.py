from django.urls import path, include

from Demo import views

urlpatterns = [
    path('index', views.index)
]
