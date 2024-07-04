from ..models.product import Product

from ..config.consts import ID_NOT_FOUND, QUANTITY_LOW, FLOATING_POINT_ERROR
from ..database import db_ops
from ..exceptions.invalid_body_exceptions import InvalidBodyException

def transform_update_quantity(product: Product) -> None:
    prod_id_quans = db_ops.get_product_ids_quans_org(product)
    if product.id not in prod_id_quans:
        raise InvalidBodyException(ID_NOT_FOUND)
    if product.quantity<0 and -product.quantity > prod_id_quans[product.id]:
        raise InvalidBodyException(QUANTITY_LOW)
    product.quantity += prod_id_quans[product.id]

def update_quantity(product: Product):
    transform_update_quantity(product)
    if product.quantity == 0 or product.quantity<FLOATING_POINT_ERROR:
        db_ops.delete_product(product)
    else:
        db_ops.quan_update(product)
