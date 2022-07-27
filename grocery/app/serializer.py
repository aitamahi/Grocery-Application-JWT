
from rest_framework import  serializers
from rest_framework.permissions import IsAuthenticated
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from .models import *

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        print(user)
        user.save()

        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = [
            'password',
        ]


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category 
        fields = '__all__'


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reviews
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Item
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Payment
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=CartItem
        fields = '__all__'


