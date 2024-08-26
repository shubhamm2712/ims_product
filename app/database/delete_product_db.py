from sqlmodel import Session, delete

from typing import List

from ..config import engine
from ..models.product import Product

class DeleteProductDB:
    def delete_products(product_org: str, product_ids: List[int]) -> None:
        with Session(engine) as session:
            statement = delete(Product).where(Product.id.in_(product_ids), Product.org == product_org, Product.usedInTransaction == 0, Product.active == 0, Product.quantity == 0.0)
            session.exec(statement)
            session.commit()
