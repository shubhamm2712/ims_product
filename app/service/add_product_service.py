from ..models.product import Product

from ..config.consts import ID_NOT_FOUND
from ..database import db_ops
from ..exceptions.invalid_body_exceptions import InvalidBodyException

def isProdUpdate(product: Product):
    if product.id:
        return True
    return False

def validateUpdate(product: Product) -> None:
    prod_ids = db_ops.get_product_ids_org(product)
    if product.id not in prod_ids:
        raise InvalidBodyException(ID_NOT_FOUND)

def add_product(product: Product):
    isUpdate = isProdUpdate(product)
    if isUpdate:
        validateUpdate(product)
        db_ops.update_product(product)
    else:
        db_ops.add_product(product)