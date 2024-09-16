from typing import List

from ..config.consts import ID_NOT_FOUND, INVALID_PRODUCT_DETAILS_TYPE, NAME_NOT_FOUND, PRODUCT_CANNOT_HAVE_NEG_OR_ZERO_QUAN, PRODUCT_CANNOT_HAVE_NEG_RATE, QUANTITY_NOT_FOUND, RATE_NOT_FOUND, USED_IN_TRANSACTION_NOT_FOUND, PRODUCT_CANNOT_HAVE_NEG_QUANTITY
from ..models.product import Product
from ..exceptions import InvalidBodyException

class ProductValidators:
    def sanitize(product: Product) -> None:
        if product.id is not None:
            if type(product.id) != int:
                raise InvalidBodyException(INVALID_PRODUCT_DETAILS_TYPE)
        if product.name is not None:
            if type(product.name) != str:
                raise InvalidBodyException(INVALID_PRODUCT_DETAILS_TYPE)
            else:
                product.name = product.name.strip()
                if product.name == "":
                    product.name = None
        if product.type is not None:
            if type(product.type) != str:
                raise InvalidBodyException(INVALID_PRODUCT_DETAILS_TYPE)
            else:
                product.type = product.type.strip()
                if product.type == "":
                    product.type = None
        if product.subtype is not None:
            if type(product.subtype) != str:
                raise InvalidBodyException(INVALID_PRODUCT_DETAILS_TYPE)
            else:
                product.subtype = product.subtype.strip()
                if product.subtype == "":
                    product.subtype = None
        if product.description is not None:
            if type(product.description) != str:
                raise InvalidBodyException(INVALID_PRODUCT_DETAILS_TYPE)
            else:
                product.description = product.description.strip()
                if product.description == "":
                    product.description = None
        if product.metaData is not None:
            if type(product.metaData) != str:
                raise InvalidBodyException(INVALID_PRODUCT_DETAILS_TYPE)
            else:
                product.metaData = product.metaData.strip()
                if product.metaData == "":
                    product.metaData = None
        if product.quantity is not None:
            if type(product.quantity) != int and type(product.quantity) != float:
                raise InvalidBodyException(INVALID_PRODUCT_DETAILS_TYPE)
        if product.avgBuyRate is not None:
            if type(product.avgBuyRate) != int and type(product.avgBuyRate) != float:
                raise InvalidBodyException(INVALID_PRODUCT_DETAILS_TYPE)

    def add_validator(product: Product) -> Product:
        ProductValidators.sanitize(product)
        if product.name is None:
            raise InvalidBodyException(NAME_NOT_FOUND)
        product.avgBuyRate = 0.0
        product.quantity = 0.0
        product.active = 1
        product.usedInTransaction = 0
        return product

    def id_validator(product: Product) -> Product:
        ProductValidators.sanitize(product)
        if product.id is None:
            raise InvalidBodyException(ID_NOT_FOUND)
        return product

    def list_id_validator(products: List[Product]) -> List[Product]:
        for product in products:
            ProductValidators.id_validator(product)
        return products
    
    def quan_validator(product: Product) -> Product:
        ProductValidators.id_validator(product)
        if product.quantity is None:
            raise InvalidBodyException(QUANTITY_NOT_FOUND)
        if product.quantity<=0:
            raise InvalidBodyException(PRODUCT_CANNOT_HAVE_NEG_OR_ZERO_QUAN)
        return product
    
    def rate_validator(product: Product) -> Product:
        ProductValidators.quan_validator(product)
        if product.avgBuyRate is None:
            raise InvalidBodyException(RATE_NOT_FOUND)
        if product.avgBuyRate<0:
            raise InvalidBodyException(PRODUCT_CANNOT_HAVE_NEG_RATE)
        return product
    
    def rollback_validator(product: Product) -> Product:
        ProductValidators.id_validator(product)
        if product.quantity is None:
            raise InvalidBodyException(QUANTITY_NOT_FOUND)
        if product.quantity<0:
            raise InvalidBodyException(PRODUCT_CANNOT_HAVE_NEG_QUANTITY)
        if product.avgBuyRate is None:
            raise InvalidBodyException(RATE_NOT_FOUND)
        if product.avgBuyRate<0:
            raise InvalidBodyException(PRODUCT_CANNOT_HAVE_NEG_RATE)
        if product.usedInTransaction is None or type(product.usedInTransaction) != int:
            raise InvalidBodyException(USED_IN_TRANSACTION_NOT_FOUND)
        if product.usedInTransaction != 0 and product.usedInTransaction != 1:
            raise InvalidBodyException(USED_IN_TRANSACTION_NOT_FOUND)
        return product