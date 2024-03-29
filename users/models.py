from django.db import models

# Create your models here.
class Empleado(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    direction = models.CharField(max_length=100)
    phone = models.IntegerField()

    def __str__(self):
        return self.first_name + ' - ' + self.last_name + ' (' + str(self.phone) + ')'

class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    direction = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.first_name + ' - ' + self.last_name + ' (' + self.email + ')'
