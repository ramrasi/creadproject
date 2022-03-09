from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.index),
    path('employee-details/<int:id>/', views.show),
    path('add-employee/', views.store),
    path('update-employee/<int:id>/', views.update),
    path('delete-employee/<int:id>/', views.destroy),
]