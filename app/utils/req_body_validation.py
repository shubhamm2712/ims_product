from ..config.consts import ID_NOT_FOUND, PRODUCT_DETAILS_MISSING_ADD, PRODUCT_DETAILS_MISSING_QUAN, PRODUCT_DETAILS_NEG_QUANTITY, INVALID_PRODUCT_DETAILS_TYPE
from ..models.product import Product
from ..exceptions.invalid_body_exceptions import InvalidBodyException

def sanitize(product: Product) -> None:
    if product.id:
        if type(product.id) != int:
            raise InvalidBodyException(INVALID_PRODUCT_DETAILS_TYPE)
    if product.name:
        if type(product.name) != str:
            raise InvalidBodyException(INVALID_PRODUCT_DETAILS_TYPE)
        else:
            product.name = product.name.strip()
    if product.type:
        if type(product.type) != str:
            raise InvalidBodyException(INVALID_PRODUCT_DETAILS_TYPE)
        else:
            product.type = product.type.strip()
    if product.subtype:
        if type(product.subtype) != str:
            raise InvalidBodyException(INVALID_PRODUCT_DETAILS_TYPE)
        else:
            product.subtype = product.subtype.strip()
    if product.description:
        if type(product.description) != str:
            raise InvalidBodyException(INVALID_PRODUCT_DETAILS_TYPE)
        else:
            product.description = product.description.strip()
    if product.metaData:
        if type(product.metaData) != str:
            raise InvalidBodyException(INVALID_PRODUCT_DETAILS_TYPE)
        else:
            product.metaData = product.metaData.strip()
    if product.quantity:
        if type(product.quantity) != float and type(product.quantity) != int:
            raise InvalidBodyException(INVALID_PRODUCT_DETAILS_TYPE)
        else:
            product.quantity = round(product.quantity, 4)
    if product.rate:
        if type(product.rate) != float and type(product.rate) != int:
            raise InvalidBodyException(INVALID_PRODUCT_DETAILS_TYPE)
        else:
            product.rate = round(product.rate, 4)

def add_product_validator(product: Product) -> Product:
    sanitize(product)
    if product.name is None or product.rate is None or product.quantity is None:
        raise InvalidBodyException(PRODUCT_DETAILS_MISSING_ADD)
    if product.quantity and product.quantity<=0:
        raise InvalidBodyException(PRODUCT_DETAILS_NEG_QUANTITY)
    return product

def update_quantity_validator(product: Product) -> Product:
    sanitize(product)
    if product.id is None or product.quantity is None:
        raise InvalidBodyException(PRODUCT_DETAILS_MISSING_QUAN)
    return product

def del_product_validator(product: Product) -> Product:
    sanitize(product)
    if product.id is None:
        raise InvalidBodyException(ID_NOT_FOUND)
    return product