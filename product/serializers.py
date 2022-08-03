
from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Product
        fields= ['pk','title' , 'content' , 'price' , 'sale_price' , 'discount']

    # def validate_title(self, value):
    #     request = request.context.get('context')
    #     user = request.user
    #     qs = Product.objects.filter(user = user , title__iexact = value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product ")
    #     return value    


    def get_discount(self, obj):
        if not hasattr(obj , 'id'):
            return None
        if not isinstance(obj , Product):
            return None    
        return obj.get_discount()

