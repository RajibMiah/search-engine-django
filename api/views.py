from django.forms.models import model_to_dict
from product.models import Product
from product.serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(["GET" , "POST" , "DELETE" , "PUT"])
def api_home(request):
    instance = Product.objects.all().order_by('?').first()
    if request.method == 'GET':
        if instance:
            data = ProductSerializer(instance).data
        return Response(data)    
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.save()
            return Response({'data':serializer.data, "msg": "Data has created"})
        return Response({"invalid":"Bad Request"} , status= 400)
