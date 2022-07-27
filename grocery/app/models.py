from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

CATEGORY_LIST=(
    ('None',"None"),
    ('FoodGrains',"FoodGrains"),#kg's
    ('Oils',"Oils"),#lits
    ('Fruits & Veg',"Fruits & Veg"),#kg's
    ('Snacks',"Snacks"),#gms
    ('Dairy Products',"Dairy Products"),#lts
    ('Personal Care',"Personal Care") #qty
)

RATING_LIST = (
    ('0','0'),
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5')
)
REVIEW_LIST =(
    ('None',"None"),
    ('0',"Excellent"),
    ('1',"Good"),
    ('2',"Average"),
    ('3',"Bad")
)
Weight_list=(
    ('0','0'),
    ('1','1Kg'),
    ('2','2Kg'),
    ('3','5Kg'),
    ('4','10Kg')
)
Volumes_list=(
    ('0','0'),
    ('1','1L'),
    ('2','2L'),
    ('3','5L'),
    ('4','10L')
)
Units_list=(
    ('0','0'),
    ('1','10cm'),
    ('2','20cm'),
    ('3','50cm'),
    ('4','100cm')
)
# Create your models here.
class Category(models.Model):
    category_item= models.CharField(max_length= 50,choices= CATEGORY_LIST,default='None',blank=True, null=True)
    
    def __str__(self):
        return self.category_item


class Item(models.Model):
    Item_name= models.CharField(max_length=100,null=True,blank=True)
    Item_category= models.ForeignKey(Category,on_delete=models.CASCADE,blank=True, null=True)
    Weights= models.CharField(max_length= 50,choices= Weight_list,default='None',blank=True, null=True)
    Volumes=models.CharField(max_length= 50,choices= Volumes_list,default='None',blank=True, null=True)
    Units=models.CharField(max_length= 50,choices= Units_list,default='None',blank=True, null=True)
    Item_max_price=models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return self.Item_name

class Reviews(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    product=models.ForeignKey(Item,on_delete=models.CASCADE,blank=True, null=True)
    reviews_item= models.CharField(max_length=10,choices=REVIEW_LIST,default='None',blank=True, null=True)
    rating_item= models.CharField(max_length=5,choices=RATING_LIST,default='0',blank=True, null=True)
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    date = models.DateTimeField(default=timezone.now,blank=True, null=True)
    order_id= models.IntegerField(blank=True,null=True)
    created_at = models.DateTimeField(default=timezone.now,blank=True, null=True)
    items = models.ManyToManyField(Item)

    def __str__(self):
        return str(self.order_id)

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()


class Payment(models.Model):
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True)
    #items = models.ManyToManyField(Products)
    payment = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True,blank=True, null=True)

    def __str__(self):
        return self.user.username

class CartItem(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    item = models.ForeignKey(Item,on_delete=models.CASCADE,blank=True, null=True)
    added_date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    
    






