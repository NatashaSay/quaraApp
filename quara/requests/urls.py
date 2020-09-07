from django.urls import path, include
from . import views
from .views import ControlView

urlpatterns = [
    path('control/', ControlView.as_view()),
]
