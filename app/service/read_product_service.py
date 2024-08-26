from typing import List

from ..config.consts import PRODUCT_DOES_NOT_EXIST
from ..database import ReadProductDB
from ..exceptions import InvalidBodyException
from ..models.product import Product

class ReadProductService:
    def get_product(product: Product) -> Product:
        product_entity = ReadProductDB.get_product(product)
        if product_entity is None:
            raise InvalidBodyException(PRODUCT_DOES_NOT_EXIST)
        return product_entity
    
    def get_all_products(product: Product) -> List[Product]:
        products = ReadProductDB.get_all_products(product)
        if products is None:
            return []
        return products
    
    def get_deleted_products(product: Product) -> List[Product]:
        products = ReadProductDB.get_deleted_products(product)
        if products is None:
            return []
        return products

    def get_products_list(product_org: str, product_ids: List[int]) -> List[Product]:
        if not product_ids:
            return []
        products = ReadProductDB.get_products_list(product_org, product_ids)
        if products is None:
            return []
        return products