from rest_framework.serializers import ModelSerializer, SerializerMethodField
from users.models import Client, Empleado



# Intermediate Serializers
class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class EmpleadoSerializer(ModelSerializer):
    class Meta:
        model = Feeding
        fields = '__all__'
        depth = 1