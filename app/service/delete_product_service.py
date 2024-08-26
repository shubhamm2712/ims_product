from typing import List

from ..database import DeleteProductDB

from ..models.product import Product

class DeleteProductService:
    def delete_products(products: List[Product]) -> None:
        if not products:
            return
        product_org = products[0].org
        product_ids = [product.id for product in products]
        DeleteProductDB.delete_products(product_org, product_ids)