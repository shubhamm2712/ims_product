from typing import Dict, Optional

from ..config.consts import PRODUCT_DOES_NOT_EXIST
from ..database import CreateProductDB, UpdateProductDB
from ..exceptions import InvalidBodyException
from ..models.product import Product

class CreateProductService:
    def add_product(product: Product) -> Product:
        if product.id is None:
            return CreateProductDB.add_product(product)
        else:
            product_entity: Optional[Product] = UpdateProductDB.update_product(product)
            if product_entity is None:
                raise InvalidBodyException(PRODUCT_DOES_NOT_EXIST)
            return product_entity