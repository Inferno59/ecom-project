from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShopHome.as_view(), name='home'),
    path('about/', views.ShopAbout.as_view(), name='about'),
]
