from ..config.consts import ORG, ORG_NOT_FOUND
from ..models.product import Product
from ..exceptions.invalid_body_exceptions import InvalidBodyException
from ..exceptions.auth_exception import UnauthorizedException

def set_org_product(product: Product, auth_result: dict) -> Product:
    if ORG in auth_result:
        product.org = auth_result[ORG]
    else:
        raise UnauthorizedException("No ORG found")
    if not product.org:
        raise InvalidBodyException(ORG_NOT_FOUND)
    return product