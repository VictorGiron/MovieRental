from django.db import models
from users.models import Client
# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    rate = models.CharField(max_length=50)
    year = models.DateField()
    description = models.TextField()
    price = models.CharField(max_length=50)

    def __str__(self):
        return self.name + ', ' + self.gender + ' (' + self.price + ')'

class RentedMovie(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    rent_date = models.DateField()
    return_date = models.DateField()

    def __str__(self):
        return self.movie + ' - ' + self.client + ' (' + self.return_date + ').'

#class