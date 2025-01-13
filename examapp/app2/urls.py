from django.urls import path
from . import views

urlpatterns = [
    path("",views.app2_list,name="list")
]
