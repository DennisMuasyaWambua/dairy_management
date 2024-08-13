from rest_framework import serializers
from users.serializer import UserSerializer
from .models import Cow, Milk


class CowSerializer(serializers.ModelSerializer):
    farmer = UserSerializer()

    class Meta:
        model = Cow
        fields = ['farmer', 'cow_name', 'breed']


class MilkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milk
        fields = '__all__'
