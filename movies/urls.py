from django.urls import path
from movies import views


urlpatterns = [
    path('movie/', views.ListCreateMovie.as_view(), name='Movies'),
    path('movie/<int:pk>/', views.RetrieveUpdateDestroyMovie.as_view(), name='Movie'),

    path('rent/', views.ListCreateRentedMovie.as_view(), name='RentedMovies'),
    path('rent/<int:pk>/', views.RetrieveUpdateDestroyRentedMovie.as_view(), name='RentedMovie'),
]