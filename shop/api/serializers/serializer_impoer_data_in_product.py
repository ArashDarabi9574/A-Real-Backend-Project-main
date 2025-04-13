from rest_framework import serializers
from shop.models.model_product import Product


class ImportDataInProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    slug = serializers.SlugField()
    main_price = serializers.IntegerField()
