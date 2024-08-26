from typing import List

from ..config.consts import ORG, ORG_NOT_FOUND
from ..models.product import Product
from ..exceptions.invalid_body_exceptions import InvalidBodyException
from ..exceptions.auth_exception import UnauthorizedException

def set_org_product(product: Product, auth_result: dict) -> Product:
    if ORG in auth_result:
        product.org = auth_result[ORG]
    else:
        raise UnauthorizedException(ORG_NOT_FOUND)
    return product

def set_org_multiple_products(products: List[Product], auth_result: dict) -> List[Product]:
    if ORG in auth_result:
        for product in products:
            product.org = auth_result[ORG]
    else:
        raise UnauthorizedException(ORG_NOT_FOUND)
    return products