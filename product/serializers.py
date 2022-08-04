from rest_framework import serializers

from .models import Product


class UserModelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    username = serializers.CharField(read_only = True)
    email = serializers.EmailField(read_only = True)
    # other_product = serializers.SerializerMethodField(read_only = True)

    # def get_other_product(self, obj):
    #     user = obj
    #     queryset= user.product_set.all()
    #     return ProductInlineSerializer(queryset , many = True , context = self.context).data


class ProductInlineSerializer(serializers.Serializer):
    # url = serializers.HyperlinkedIdentityField(
    #     view_name='product-details',
    #     lookup_field= 'pk',
    #     read_only = True
    # )
    id = serializers.IntegerField(read_only = True)
    title = serializers.CharField(read_only = True)

class ProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only = True)
    owner = UserModelSerializer( source = 'user',read_only = True)
    class Meta:
        model = Product
        fields= ['owner','pk','title' , 'content' , 'price' , 'sale_price' , 'discount' ]

    def get_discount(self, obj):
        return obj.get_discount()
