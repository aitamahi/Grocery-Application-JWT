from django.urls import path, include,re_path
from .api import *
from .views import *


urlpatterns=[
    re_path(r'login/',login_user,name='login'),
    re_path(r'logout/',User_logout,name='logout'),
    path(r'register/', RegisterApi.as_view()),   
    path(r'category/', CreateCategories.as_view()), 
    path(r'order/', OrderItem.as_view()),
    path(r'item/', AddProducts.as_view()),
    path(r'item/<int:pk>/', AddProducts.as_view()),
    path(r'review/', AddReview.as_view()),
    path(r'payment/', AddPayment.as_view()),
    path(r'cart/', AddCartItem.as_view()),
    path(r'item1/<int:pk>/', ProductsSearch.as_view()),
    path(r'order_list/', OrderList.as_view()),
    path(r'itemfetch/',ItemsFetch.as_view()),
    
]
