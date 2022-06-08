from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('MobileRecharge', views.MobileRecharge, name='MobileRecharge'),
    path('DthRecharge', views.DthRecharge, name='DthRecharge'),
    path('History', views.History, name='History'),
    path('Login', views.Login, name='Login'),
    
]
