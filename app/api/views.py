from rest_framework import generics, status
from rest_framework.response import Response

from app import models
from app.api import serializers


class DogList(generics.ListCreateAPIView):
    serializer_class = serializers.DogSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = serializers.DogSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        return models.Dog.objects.filter(owner__user=self.request.user)

    def post(self, request, *args, **kwargs):
        serializer = serializers.DogSerializer(data=request.data)
        if serializer.is_valid():
            owner = models.Owner.objects.get(user=self.request.user)
            serializer.save(owner=owner)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Dog.objects.all()
    serializer_class = serializers.DogSerializer


class CatList(generics.ListCreateAPIView):
    serializer_class = serializers.CatSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = serializers.CatSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        return models.Cat.objects.filter(owner__user=self.request.user)

    def post(self, request, *args, **kwargs):
        serializer = serializers.CatSerializer(data=request.data)
        if serializer.is_valid():
            owner = models.Owner.objects.get(user=self.request.user)
            serializer.save(owner=owner)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Cat.objects.all()
    serializer_class = serializers.CatSerializer
