from ..models.product import Product

from ..database import db_ops
from ..exceptions.invalid_body_exceptions import InvalidBodyException

def transform_update_quantity(product: Product) -> None:
    prod_id_quans = db_ops.get_product_ids_quans_org(product)
    if product.id not in prod_id_quans:
        raise InvalidBodyException("Invalid product id")
    if product.quantity<0 and -product.quantity > prod_id_quans[product.id]:
        raise InvalidBodyException("Quantity cannot be deleted")
    product.quantity += prod_id_quans[product.id]

def update_quantity(product: Product):
    transform_update_quantity(product)
    db_ops.quan_update(product)
