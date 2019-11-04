from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from movies.models import Movie, RentedMovie
# Create your views here.
#Movie
class ListCreateMovie(ListCreateAPIView):
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieDetailSerializer
        elif self.request.method == 'POST':
            return MovieSerializer


class RetrieveUpdateDestroyMovie(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieDetailSerializer
        elif self.request.method == 'PATCH' or self.request.method == 'PUT':
            return MovieSerializer

#RentedMovie
class ListCreateRentedMovie(ListCreateAPIView):
    queryset = RentedMovie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RentedMovieDetailSerializer
        elif self.request.method == 'POST':
            return RentedMovieSerializer


class RetrieveUpdateDestroyRentedMovie(RetrieveUpdateDestroyAPIView):
    queryset = RentedMovie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RentedMovieDetailSerializer
        elif self.request.method == 'PATCH' or self.request.method == 'PUT':
            return RentedMovieSerializer