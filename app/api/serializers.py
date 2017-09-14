from rest_framework import serializers
from app import models


class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Dog
        fields = ['name', 'birthday', 'owner']


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cat
        fields = ['name', 'birthday', 'owner']