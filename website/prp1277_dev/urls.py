from django.urls import path
from prp1277_dev import views

urlpatterns = [
    path("", views.home, name="home"),
]
