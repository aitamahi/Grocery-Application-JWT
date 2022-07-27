from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display= ['id','category_item']


class ReviewsAdmin(admin.ModelAdmin):
    list_display= ['id','user','product','reviews_item','rating_item']


class ItemAdmin(admin.ModelAdmin):
    list_display= ['id','Item_name','Item_category','Weights','Volumes','Units','Item_max_price']


class OrderAdmin(admin.ModelAdmin):
    list_display= ['id','user','date','order_id','created_at']


class CartAdmin(admin.ModelAdmin):
    list_display= ['id','user','item','added_date']


class PaymentAdmin(admin.ModelAdmin):
    list_display= ['id','order_id','user','payment','timestamp']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Reviews,ReviewsAdmin)
admin.site.register(Item,ItemAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(CartItem,CartAdmin)
admin.site.register(Payment,PaymentAdmin)
