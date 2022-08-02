
from rest_framework import  serializers
from django.db import models
from django.contrib.auth.models import User
from .models import *

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
  

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


