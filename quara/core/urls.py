from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit, name='edit'),
    path('health/', views.health, name='health'),
    path('monitoring/', views.monitoring, name='monitoring'),
    path('call/', views.call, name='call'),

    path('mycalls/', views.mycalls, name='mycalls'),

    path('deletemonitoring/<int:pk>/', views.deletemonitoring, name='delete-monitoring'),
    path('book/<int:pk>/', views.book, name='book'),
    path('confirm/<int:pk>/', views.confirm, name='confirm'),


    path('cancellcall/<int:pk>/', views.cancellcall, name='cancellcall'),

    path('shops/', views.shops, name='shops'),

    path('statistics/', views.statistics, name='statistics'),


    
    #path('book/<int:pk>/', views.book, name='book'),
]
