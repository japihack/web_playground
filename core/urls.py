from django.urls import path
from .views import Home, Sample

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('sample/', Sample.as_view(), name="sample")
]