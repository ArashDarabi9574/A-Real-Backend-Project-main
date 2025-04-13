from shop.models import Discount
from shop.models.model_order import Order


def apply_discount(discount_code: Discount, order: Order) -> str:

    type_discount = discount_code.type_discount
    total_price = order.get_total_price

    if type_discount == 0:
        discount_amount = int((total_price * discount_code.percentage) / 100)
        total_paid_price = total_price - discount_amount
    else:
        total_paid_price = total_price - discount_code.amount_discount

    order.total_paid_price = total_paid_price
    order.save()
