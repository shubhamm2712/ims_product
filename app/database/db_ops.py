from sqlmodel import Session, select
from typing import Set, Dict, List

from .db_config import engine

from ..models.product import Product

def get_products(product: Product) -> Dict[int, Product]:
    prods = dict()
    with Session(engine) as session:
        statement = select(Product).where(Product.org == product.org)
        results = session.exec(statement)
        for prod in results:
            prods[prod.id] = prod
    return prods

def get_product_ids_org(product: Product) -> Set[int]:
    prod_ids = set()
    with Session(engine) as session:
        statement = select(Product.id).where(Product.org == product.org)
        results = session.exec(statement)
        for id in results:
            prod_ids.add(id)
    return prod_ids

def get_product_ids_quans_org(product: Product) -> Dict:
    prods = dict()
    with Session(engine) as session:
        statement = select(Product.id, Product.quantity).where(Product.org == product.org)
        results = session.exec(statement)
        for id,quan in results:
            prods[id] = quan
    return prods

def add_product(product: Product) -> Product:
    with Session(engine) as session:
        session.add(product)
        session.commit()
        session.refresh(product)
    return product

def update_product(product: Product) -> Product:
    with Session(engine) as session:
        db_product = session.get(Product, product.id)
        if db_product.id == product.id and db_product.org == product.org:
            db_product.update(product)
        session.add(db_product)
        session.commit()
        session.refresh(db_product)
    return db_product

def delete_product(product: Product) -> None:
    with Session(engine) as session:
        product = session.get(Product, product.id)
        session.delete(product)
        session.commit()

def quan_update(product: Product) -> Product:
    with Session(engine) as session:
        new_quantity = product.quantity
        product = session.get(Product, product.id)
        product.quantity = new_quantity
        session.add(product)
        session.commit()
        session.refresh(product)
    return product