
from django.urls import path,include

urlpatterns = [
    path("v1/",include("main_func.api.v1.urls"))
]
