from django.urls import path
from . import views

urlpatterns = [
    path('bookingform', views.bookroom, name = 'bookingform'),
]