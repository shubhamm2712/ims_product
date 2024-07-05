from typing import Optional

from ..config.consts import ID_NOT_FOUND, PRODUCT_DETAILS_MISSING_ADD, PRODUCT_DETAILS_MISSING_UPDATE, PRODUCT_DETAILS_MISSING_QUAN
from ..models.product import Product
from ..exceptions.invalid_body_exceptions import InvalidBodyException

def sanitize(product: Product):
    all_attributes = dir(Product)
    attributes = [attribute for attribute in all_attributes if not attribute.startswith('_')]
    for attribute in attributes:
        value: str = getattr(product, attribute)
        if value and type(value)==str:
            value = value.strip()
            if not value:
                value = None
            setattr(product, attribute, value)

def add_product_validator(product: Product):
    sanitize(product)
    if product.id is None:
        if product.name is None or product.rate is None or product.quantity is None:
            raise InvalidBodyException(PRODUCT_DETAILS_MISSING_ADD)
    else:
        if not (product.name or product.type or product.subtype or product.metaData or product.description or product.quantity or product.rate):
            raise InvalidBodyException(PRODUCT_DETAILS_MISSING_UPDATE)
    return product

def update_quantity_validator(product: Product):
    sanitize(product)
    if product.id is None or product.quantity is None:
        raise InvalidBodyException(PRODUCT_DETAILS_MISSING_QUAN)
    return product

def del_product_validator(product: Product):
    sanitize(product)
    if product.id is None:
        raise InvalidBodyException(ID_NOT_FOUND)
    return product