from sqlmodel import Session

from ..config import engine
from ..models.product import Product

class CreateProductDB:
    def add_product(product: Product) -> Product:
        with Session(engine) as session:
            session.add(product)
            session.commit()
            session.refresh(product)
            return product