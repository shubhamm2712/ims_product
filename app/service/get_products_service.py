from typing import List

from ..models.product import Product

from ..database import db_ops

def get_products(product: Product) -> List[Product]:
    return db_ops.get_products(product)