from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters
from rest_framework.response import Response
import django_filters



from shop.api.serializers import (
    ProductCreateUpdateSerializer,
    ProductListSerializer,
    ProductDetailSerializer,
    TorobProductSerializer
)
from shop.models import Product, ProductsCollections
from drf_spectacular.utils import extend_schema
from core.pagination import CustomPagination, CustomPaginationTorob
from django.db.models import Case, IntegerField, Value, When
from utils.general.models.model_status_abstract import Choices



class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(
        field_name='main_price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(
        field_name='main_price', lookup_expr='lte')
    collections = django_filters.CharFilter(
        method='filter_by_collections', label='Collections')
    brands = django_filters.CharFilter(
        method='filter_by_brands', label='brands')

    discount_active = django_filters.BooleanFilter(
        method='filter_discount_active', label="discount active?")
    in_invetory = django_filters.BooleanFilter(
        method='filter_in_invetory', label="محصولات موجود")

    class Meta:
        model = Product
        fields = ['min_price', 'max_price', 'status', 'brands',
                  'discount_active', 'collections', 'in_invetory']

    def filter_discount_active(self, queryset, name, value):
        if value is True:
            return queryset.filter(deadline_price__isnull=False)
        elif value is False:
            return queryset.filter(deadline_price__isnull=True)
        return queryset

    def filter_in_invetory(self, queryset, name, value):
        if value is True:
            queryset = queryset.filter(product_branch__inventory__gt=0)
        return queryset

    # AND
    # def filter_by_collections(self, queryset, name, value):
    #     if value:
    #         # Split input string into a list of collection IDs
    #         collections_list = value.split(',')
    #         for collection in collections_list:
    #             queryset = queryset.filter(collections__id=collection)
    #         return queryset
    #     return queryset
    
    # OR
    def filter_by_collections(self, queryset, name, value):
        if value:
            # Split input string into a list of collection IDs
            collections_list = value.split(',')
            final_collections = dict()
            for collection in collections_list:
                my_collection = ProductsCollections.objects.get(id=collection)
                parent_id = str(my_collection.parent.id)
                if final_collections.get(parent_id) is not None:
                    final_collections[parent_id].append(my_collection.id)
                else:
                    final_collections[parent_id] = [my_collection.id]
            for values in final_collections.values():
                queryset = queryset.filter(collections__id__in=values)
            return queryset
        return queryset

    def filter_by_brands(self, queryset, name, value):
        if value:
            # Split input string into a list of collection IDs
            brands_list = value.split(',')
            return queryset.filter(brand__id__in=brands_list)
        return queryset


@extend_schema(tags=["Products"])
class ProductViewSet(viewsets.ModelViewSet):
    model = Product
    serializer_class = ProductDetailSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'post', 'delete', 'patch']
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['slug', 'title', 'collections__title']
    filterset_class = ProductFilter
    ordering = ('-status', '-created_at', '-total_sold')
    ordering_fields = ['main_price', 'created_at', 'total_sold', 'status']

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return ProductCreateUpdateSerializer
        return self.serializer_class

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAdminUser()]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

@extend_schema(tags=["Products"])
class ProductTorob(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = TorobProductSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get']
    pagination_class = CustomPaginationTorob

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


