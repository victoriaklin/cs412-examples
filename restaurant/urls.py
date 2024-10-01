from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view, name='home'),
    path('main/', views.main_view, name='main'),
    path('order/', views.order_view, name='order'),  
    path('confirmation/', views.confirmation, name='confirmation')
]