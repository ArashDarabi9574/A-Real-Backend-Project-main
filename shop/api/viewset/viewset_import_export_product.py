import csv

from drf_spectacular.utils import extend_schema
from rest_framework import views
from shop.models import Product
from rest_framework import permissions
from utils.response import unsuccessful_response, successful_response
from utils.export_csv_from_table import export_data_from_product_table
from utils.import_csv_from_table import import_data_in_product_table


@extend_schema(tags=["Import/Export"])
class ImportExportProductView(views.APIView):
    model = Product
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        return export_data_from_product_table(
            queryset=self.model.objects.all(),
            fields=['id', 'title', 'slug', 'main_price'],
            csv_file_name='list_product'
        )

    def post(self, request):
        file = request.FILES['file']
        if not file:
            return unsuccessful_response(message='ارسال فایل اجباری است.', data={})

        import_data_in_product_table(file=file)
        return successful_response(message=f'update is successful .', data={})
