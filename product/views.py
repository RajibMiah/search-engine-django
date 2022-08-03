
from rest_framework import generics

from .mixins import StaffEditorPermissionMixin, UserQuerysetMixin
from .models import Product
from .serializers import ProductSerializer


# Create your views here.
class ProductDetailsApiView( UserQuerysetMixin,  StaffEditorPermissionMixin , generics.ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field ='pk'


    def perform_create(self , serializer):
        print('titile' , serializer)
        title = serializer.validated_data['title']
        content = serializer.validated_data['content'] or None

        if content is None:
            content = title
        serializer.save(user = self.request.user , content = content)

    # def get_queryset(self , *args , **kwargs):
    #     qs = super().get_queryset( *args , **kwargs)
    #     request = self.request
    #     user = request.user
    #     print("user", user)
    #     if not user.is_authenticated:
    #         print('not authenticated')
    #         return Product.objects.none()
    #     print('user authenticated')        
    #     return qs.filter(user = user)
