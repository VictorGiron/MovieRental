from django.urls import path
from users import views


urlpatterns = [
    path('user/', views.ListCreateClient.as_view(), name='Clients'),
    path('user/<int:pk>/', views.RetrieveUpdateDestroyClient.as_view(), name='Client'),

    path('user/empleado/', views.ListCreateEmpleado.as_view(), name='Empleados'),
    path('user/empleado/<int:pk>/', views.RetrieveUpdateDestroyEmpleado.as_view(), name='Empleado'),
]