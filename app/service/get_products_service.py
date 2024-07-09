from typing import List

from ..models.product import Product

from ..database import db_ops

def get_products(product: Product) -> List[Product]:
    prods_dict = db_ops.get_products(product)
    return list(prods_dict.values())