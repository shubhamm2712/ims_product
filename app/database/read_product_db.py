from sqlmodel import Session, select

from typing import List, Optional

from ..config import engine
from ..models.product import Product

class ReadProductDB:
    def get_product(product: Product) -> Optional[Product]:
        with Session(engine) as session:
            statement = select(Product).where(Product.id == product.id, Product.org == product.org)
            results = session.exec(statement)
            return results.first()
    
    def get_all_products(product: Product) -> List[Product]:
        with Session(engine) as session:
            statement = select(Product).where(Product.org == product.org, Product.active == 1)
            results = session.exec(statement)
            return results.all()
        
    def get_deleted_products(product: Product) -> List[Product]:
        with Session(engine) as session:
            statement = select(Product).where(Product.org == product.org, Product.active == 0)
            results = session.exec(statement)
            return results.all()
    
    def get_products_list(product_org: str, product_ids: List[int]) -> List[Product]:
        with Session(engine) as session:
            statement = select(Product).where(Product.org == product_org, Product.id.in_(product_ids))
            results = session.exec(statement)
            return results.all()