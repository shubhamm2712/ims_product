from ..models.product import Product

from ..config.consts import ID_NOT_FOUND
from ..database import db_ops
from ..exceptions.invalid_body_exceptions import InvalidBodyException

def validateUpdate(product: Product) -> None:
    prod_ids = db_ops.get_product_ids_org(product)
    if product.id not in prod_ids:
        raise InvalidBodyException(ID_NOT_FOUND)

def del_product(product: Product):
    validateUpdate(product)
    db_ops.delete_product(product)