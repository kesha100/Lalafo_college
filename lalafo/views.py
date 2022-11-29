from django.shortcuts import render
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import filters

class ProductListAPIView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['product', 'description']
    def get_queryset(self):
        try:
            return Product.objects.filter(id=self.kwargs['pk'])
        except:
            return Product.objects.all()
    #
    # def list(self, request, *args, **kwargs):
    #
    #     queryset = Product.objects.filter(product__icontains=request.GET.get('product', ''))
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)
    class CustomSearchFilter(filters.SearchFilter):
        def get_search_fields(self, view, request):
            if request.query_params.get('title_only'):
                return ['title']
            return super().get_search_fields(view, request)

