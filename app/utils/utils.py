from ..config.consts import ORG, ORG_NOT_FOUND
from ..models.product import Product
from ..exceptions.invalid_body_exceptions import InvalidBodyException

def set_org_product(product: Product, auth_result: dict):
    if ORG in auth_result:
        product.org = auth_result[ORG]
    if not product.org:
        raise InvalidBodyException(ORG_NOT_FOUND)
    return product