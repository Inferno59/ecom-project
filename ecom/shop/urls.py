from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShopHome.as_view()),
]
