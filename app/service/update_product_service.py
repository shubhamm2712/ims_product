from typing import List, Optional

from ..config.consts import PRODUCT_DETAILS_NEG_QUANTITY, PRODUCT_DOES_NOT_EXIST
from ..database import UpdateProductDB
from ..exceptions import InvalidBodyException
from ..models.product import Product

class UpdateProductService:
    def deactivate_products(products: List[Product]) -> None:
        if not products:
            return
        product_org = products[0].org
        product_ids = [product.id for product in products]
        UpdateProductDB.deactivate_products(product_org, product_ids)
    
    def recover_products(products: List[Product]) -> None:
        if not products:
            return
        product_org = products[0].org
        product_ids = [product.id for product in products]
        UpdateProductDB.recover_products(product_org, product_ids)

    def add_product_quantity(product: Product) -> Product:
        product_entity = UpdateProductDB.add_quantity(product)
        if product_entity is None:
            raise InvalidBodyException(PRODUCT_DOES_NOT_EXIST)
        return product_entity

    def del_product_quantity(product: Product) -> Product:
        product_entity: Optional[Product] = UpdateProductDB.del_quantity(product)
        if product_entity is None:
            raise InvalidBodyException(PRODUCT_DOES_NOT_EXIST)
        if product_entity.quantity == -1:
            raise InvalidBodyException(PRODUCT_DETAILS_NEG_QUANTITY)
        return product_entity
    
    def rollback_product_quantity(product: Product) -> Product:
        product_entity: Optional[Product] = UpdateProductDB.rollback_quantity(product)
        if product_entity is None:
            raise InvalidBodyException(PRODUCT_DOES_NOT_EXIST)
        return product_entity