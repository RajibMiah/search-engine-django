
from django.shortcuts import get_object_or_404
from product.models import Product
from product.serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(["GET" , "POST" , "DELETE" , "PUT"])
def api_home(request, pk = None):
    print('yess')
    if request.method == 'GET':
        if pk is not None:
            obj = get_object_or_404(Product , pk = pk)
            data = ProductSerializer(obj).data
            return Response(data)    
        queryset = Product.objects.all()   
        data = ProductSerializer(queryset , many=True).data
        return Response(data)    

    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.save()
            return Response({'data':serializer.data, "msg": "Data has created"})
        return Response({"invalid":"Bad Request"} , status= 400)
