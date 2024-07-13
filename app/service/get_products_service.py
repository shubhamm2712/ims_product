from typing import List

from ..config.consts import ID_NOT_FOUND

from ..exceptions.invalid_body_exceptions import InvalidBodyException

from ..models.product import Product

from ..database import db_ops

def get_products(product: Product) -> List[Product]:
    prods_dict = db_ops.get_products(product)
    return list(prods_dict.values())

def get_product(product: Product) -> Product:
    product = db_ops.get_product(product)
    if product is None:
        raise InvalidBodyException(ID_NOT_FOUND)
    return product