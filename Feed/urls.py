from django.urls import path
from . import views

app_name = "Feed"

urlpatterns = [
    path("", views.HomePage.as_view(), name= "index")
]