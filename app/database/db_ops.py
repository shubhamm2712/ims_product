from sqlmodel import Session, select
from typing import Set, Dict, List

from .db_config import engine

from ..models.product import Product

def get_products(product: Product) -> List[Product]:
    prods = []
    with Session(engine) as session:
        statement = select(Product).where(Product.org == product.org)
        results = session.exec(statement)
        for prod in results:
            prods.append(prod)
    return prods

def get_product_ids_org(product: Product) -> Set:
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
        # Can add code to not delete already set properties by using model_dump of sqlmodel
        session.add(product)
        session.commit()
        session.refresh(product)
    return product

def delete_product(product: Product) -> None:
    with Session(engine) as session:
        product = session.get(Product, product.id)
        session.delete(product)
        session.commit()

def quan_update(product: Product) -> Product:
    with Session(engine) as session:
        new_quantity = product.quantity
        if new_quantity == 0 or abs(new_quantity-0)<10e-3: # for floating point errors
            delete_product(product)
        else:
            product = session.get(Product, product.id)
            product.quantity = new_quantity
            session.add(product)
            session.commit()
            session.refresh(product)
    return product