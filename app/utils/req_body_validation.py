from typing import Optional

from ..models.product import Product
from ..exceptions.invalid_body_exceptions import InvalidBodyException

def add_product_validator(product: Product):
    if product.id is None:
        if product.name is None or product.rate is None or product.quantity is None:
            raise InvalidBodyException("Product details missing in add product request")
    else:
        if not (product.name or product.type or product.subtype or product.meta_data or product.description or product.quantity or product.rate):
            raise InvalidBodyException("Product details missing to update product request")
    return product

def del_product_validator(product: Product):
    if product.id is None:
        raise InvalidBodyException("Id is not present in delete product request")
    else:
        if product.quantity is None:
            raise InvalidBodyException("Product quantity missing to be deleted from product")
    return product