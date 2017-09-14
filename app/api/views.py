from rest_framework import generics, mixins
from app import models
from app.api import serializers


class DogList(generics.ListCreateAPIView):
    queryset = models.Dog.objects.all()
    serializer_class = serializers.DogSerializer


class DogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Dog.objects.all()
    serializer_class = serializers.DogSerializer


class CatList(generics.ListCreateAPIView):
    queryset = models.Cat.objects.all()
    serializer_class = serializers.CatSerializer


class CatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Cat.objects.all()
    serializer_class = serializers.CatSerializer
