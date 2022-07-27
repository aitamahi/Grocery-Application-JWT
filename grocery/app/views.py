from django.shortcuts import render
from .serializer import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.db import IntegrityError
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
import json
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import views, response, exceptions, permissions
from .models import *
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
import sys
from rest_framework import status
from django.db.models import Q
from rest_framework import generics
from rest_framework import filters
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt)
@api_view(["POST"])
@permission_classes([AllowAny])
def login_user(request):
    data = {}
    #import pdb; pdb.set_trace()
    print(request.data)
    uname = request.data['username']
    password = request.data['password']
    try:
        Account = User.objects.get(username=uname)
    except BaseException as e:
        raise ValidationError({"400": f'{str(e)}'})

    Token.objects.filter(user=Account).delete()
    token = Token.objects.get_or_create(user=Account)[0].key
    print(token)
    if password != password:
        raise ValidationError({"message": "Incorrect Login credentials"})

    if Account:
        if Account.is_active:
            login(request, Account)
            data["message"] = "user logged in"
            data["email_address"] = Account.username
            data["id"]=Account.id

            Res = {"data": data, "token": token}
            return Response(Res)

        else:
            raise ValidationError({"400": f'Account not active'})

    else:
        raise ValidationError({"400": f'Account doesnt exist'})

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def User_logout(request):
    request.user.auth_token.delete()
    logout(request)
    return Response('User Logged out successfully')

#from django.http import HttpResponseRedirect

# def Home(request):
#     return render(request,'Home.html',locals())
    
class CreateCategories(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
            data = {}
            serializer = CategorySerializer(data=request.data)
            if serializer.is_valid():
                category = serializer.save()
                category.save()
                if category:
                    data['id'] = category.id
                    data['category_item'] = category.category_item
                    
            else:
                data = serializer.errors
            return Response(data)
        except KeyError as e:
            print(e)
            raise ValidationError({"400": f'Field {str(e)} missing'})


class AddPayment(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        try:
            data = {}
            serializer = PaymentSerializer(data=request.data)
            #import pdb; pdb.set_trace()
            if serializer.is_valid():
                Item = serializer.save()
                Item.save()

            else:
                data = serializer.errors
            return Response(serializer.data)
        except KeyError as e:
            print(e)
            raise ValidationError({"400": f'Field {str(e)} missing'})

class AddProducts(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self, pk):
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        #id = self.request.query_params.get('id')
        id = self.get_object(pk)
        serializer = ItemSerializer(id)
        return Response(serializer.data)

    def post(self, request):
        try:
            #import pdb; pdb.set_trace()
            data = {}
            serializer = ItemSerializer(data=request.data)
            #print(serializer)
            if serializer.is_valid():
                item = serializer.save()
                item.save()
                return Response(serializer.data)
            else:
                data = serializer.errors
                raise ValidationError({"400"})

        except KeyError as e:
            print(e)
            raise ValidationError({"400": f'Field {str(e)} missing'})


class AddReview(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


    def post(self,request):
        try:
            data = {}
            serializer = ReviewsSerializer(data=request.data)
            #import pdb; pdb.set_trace()
            if serializer.is_valid():
                Item = serializer.save()
                Item.save()

            else:
                data = serializer.errors
            return Response(serializer.data)
        except KeyError as e:
            print(e)
            raise ValidationError({"400": f'Field {str(e)} missing'})

class OrderItem(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data, context={'request': request})
        #import pdb; pdb.set_trace()
        if serializer.is_valid(raise_exception=ValueError):
            user = request.user
            obj = Order()
            obj.user = user
            obj.date = request.data['date']
            obj.order_id = request.data['order_id']
            obj.created_at = request.data['created_at']
            
            obj.save()
            for i in request.data['items']:
                product = Item.objects.get(id=i)
                obj.items.add(product)

            #published_item = serializer.create(validated_data=request.data, user=user)
            try:

                return Response({obj.id:serializer.data}, status=status.HTTP_201_CREATED)
            except Exception as e:
                print(e)
                return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

#@method_decorator(csrf_exempt)
class AddCartItem(APIView):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        try:
            data = {}
            serializer = CartItemSerializer(data=request.data)
            #import pdb; pdb.set_trace()
            if serializer.is_valid():
                product = serializer.save()
                product.save()

            else:
                data = serializer.errors
            return Response(data)
        except KeyError as e:
            print(e)
            raise ValidationError({"400": f'Field {str(e)} missing'})




class ProductsSearch(generics.ListCreateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ['id']
    filter_backends = (filters.SearchFilter,)
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class OrderList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # import pdb; pdb.set_trace()
        # print(self.request.query_params)
        user = request.user

        orders = Order.objects.filter(user = user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)


class ItemsFetch(generics.ListCreateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        import pdb; pdb.set_trace()
        name = self.request.query_params.get('name')
        try:
            price = self.request.query_params.get('price')
        except:
            pass
        category = self.request.query_params.get('category')
        rating = self.request.query_params.get('rating')

        orders = Item.objects.filter(Q(Item_name__icontains = name) | Q(Item_category = category) | Q(Item_max_price=price)).values('Item_name','Item_category','Item_max_price')
        serializer = OrderSerializer(orders, many=True)
        return Response(orders)

