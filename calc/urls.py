from django.urls import path
from . import views


urlpatterns = [

    path("", views.home, name = "home"),
    path('cal', views.cal, name = "cal" ),
    path('add', views.add, name = "add")

]