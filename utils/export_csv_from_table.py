import csv
from datetime import datetime
from typing import List
from django.db import models
from django.http import HttpResponse


def export_data_from_product_table(queryset: models.QuerySet, fields: List[str], csv_file_name) -> str:
    try:
        date = datetime.now().strftime("%Y_%m_%d")

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{csv_file_name}_date_{date}_export.csv"'
        writer = csv.DictWriter(response, fieldnames=fields)
        writer.writeheader()

        for _object in queryset.values(*fields):
            writer.writerow(_object)

        return response

    except Exception as e:
        return str(e)
