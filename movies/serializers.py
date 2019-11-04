from rest_framework.serializers import ModelSerializer, SerializerMethodField
from movies.models import RentedMovie, Movie

class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class RentedMovieSerializer(ModelSerializer):
    class Meta:
        model = RentedMovie
        fields = '__all__'
        depth = 1
