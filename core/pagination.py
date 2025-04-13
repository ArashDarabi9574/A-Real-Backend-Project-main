from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 24
    page_query_param = 'page'
    max_page_size = 100

class CustomPagination2(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
    max_page_size = 100

class CustomPaginationTorob(PageNumberPagination):
    page_size = 100
    page_query_param = 'page'
    max_page_size = 100
