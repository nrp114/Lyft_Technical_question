from django.urls import path, include

from Demo import views

urlpatterns = [
    path('test', views.index)
]
