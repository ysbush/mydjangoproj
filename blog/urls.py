from django.urls import path
from . import views #.은 현재 폴더(elections)를 의미합니다.

urlpatterns = [
    
    path('', views.index)
]