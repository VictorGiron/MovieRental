from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from users.models import Client, Empleado
# Create your views here.
#Client
class ListCreateClient(ListCreateAPIView):
    queryset = Client.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ClientDetailSerializer
        elif self.request.method == 'POST':
            return ClientSerializer


class RetrieveUpdateDestroyClient(RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ClientDetailSerializer
        elif self.request.method == 'PATCH' or self.request.method == 'PUT':
            return ClientSerializer

#Empleado
class ListCreateEmpleado(ListCreateAPIView):
    queryset = Empleado.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return EmpleadoDetailSerializer
        elif self.request.method == 'POST':
            return EmpleadoSerializer


class RetrieveUpdateDestroyEmpleado(RetrieveUpdateDestroyAPIView):
    queryset = Empleado.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return EmpleadoDetailSerializer
        elif self.request.method == 'PATCH' or self.request.method == 'PUT':
            return EmpleadoSerializer