import csv

from shop.models import Product
from shop.api.serializers.serializer_impoer_data_in_product import ImportDataInProductSerializer
from utils.response import unsuccessful_response


def import_data_in_product_table(file: str):
    decoded_file = file.read().decode('utf-8').splitlines()
    reader = csv.DictReader(decoded_file)

    for row in reader:
        print('************************')
        serialize_data = ImportDataInProductSerializer(data=row)
        if not serialize_data.is_valid():
            return unsuccessful_response(message=serialize_data.errors, data={})

        _object = Product.objects.filter(pk=serialize_data.validated_data.get('id')).last()
        if _object is not None:
            _object.main_price = serialize_data.validated_data.get('main_price')
            _object.save()
