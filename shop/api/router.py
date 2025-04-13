from rest_framework import routers
from django.urls import path, include
from shop.api import viewset

router = routers.DefaultRouter()
router.register('product', viewset.ProductViewSet, basename='product')
router.register('product-torob', viewset.ProductTorob, basename='product-torob')
router.register('sending-method', viewset.SendingMethodViewSet, basename='sending-method')
router.register('order/item', viewset.OrderItemViewSet, basename='item')
router.register('order', viewset.OrderViewSet, basename='order')
router.register('user_order', viewset.UserOrderViewSet, basename='user_order')
router.register('comment', viewset.CommentViewSet, basename='comment')
router.register('discount', viewset.DiscountViewSet, basename='discount')
router.register('collection', viewset.CollectionViewSet, basename='collection')
router.register('brand', viewset.BrandViewSet, basename='brand')
router.register('special_tag', viewset.SpecialTagViewSet,
                basename='special_tag')
router.register('suggestion', viewset.SuggestionViewSet, basename='suggestion')
router.register('branch', viewset.BranchViewSet, basename='branch')
router.register('color', viewset.ColorViewSet, basename='color')
router.register('attribute_style', viewset.AttributeStyleViewSet,
                basename='attribute_style')
router.register('attribute_style_normal', viewset.AttributeStyleListViewSet,
                basename='attribute_style_normal')
router.register('attribute_tech', viewset.AttributeTechViewSet,
                basename='attribute_tech')
router.register('reminder', viewset.ReminderView, basename='reminder')


urlpatterns = [
    path('invoice/', viewset.InvoiceView.as_view(), name='invoice'),
    path('import-export-data/product/', viewset.ImportExportProductView.as_view(), name='import_export'),
    path('request_payment/', viewset.RequestPayment.as_view(),
         name='request_payment'),
    path('', include(router.urls)),
]
