from sqlmodel import Session, select, update

from typing import Optional, List

from ..config.consts import ROUNDING_FACTOR
from ..config import engine
from ..models.product import Product

class UpdateProductDB:
    def update_product(product: Product) -> Optional[Product]:
        with Session(engine) as session:
            statement = select(Product).where(Product.id == product.id, Product.org == product.org, Product.active == 1)
            results = session.exec(statement)
            db_product = results.first()
            if db_product is None:
                return None
            db_product.update(product)
            session.add(db_product)
            session.commit()
            session.refresh(db_product)
            return db_product

    def deactivate_products(product_org: str, product_ids: List[int]) -> None:
        with Session(engine) as session:
            statement = update(Product).where(Product.id.in_(product_ids), Product.org == product_org, Product.usedInTransaction == 0, Product.quantity == 0.0).values(active = 0)
            session.exec(statement)
            session.commit()
    
    def recover_products(product_org: str, product_ids: List[int]) -> None:
        with Session(engine) as session:
            statement = update(Product).where(Product.id.in_(product_ids), Product.org == product_org, Product.active == 0).values(active = 1)
            session.exec(statement)
            session.commit()

    def add_quantity(product: Product) -> Optional[Product]:
        with Session(engine) as session:
            statement = select(Product).where(Product.id == product.id, Product.org == product.org, Product.active == 1)
            results = session.exec(statement)
            db_product = results.first()
            if db_product is None:
                return None
            original_quantity = db_product.quantity
            original_rate = db_product.avgBuyRate
            original_used_in_trans =  db_product.usedInTransaction
            current_total_buy_cost = db_product.quantity * db_product.avgBuyRate
            current_total_buy_cost += product.quantity * product.avgBuyRate
            db_product.quantity = round(db_product.quantity + product.quantity, ROUNDING_FACTOR)
            db_product.avgBuyRate = round(current_total_buy_cost/db_product.quantity, ROUNDING_FACTOR)
            db_product.active = 1
            db_product.usedInTransaction = 1
            session.add(db_product)
            session.commit()
            session.refresh(db_product)
            db_product.quantity = original_quantity
            db_product.avgBuyRate = original_rate
            db_product.usedInTransaction = original_used_in_trans
            return db_product
    
    def del_quantity(product: Product) -> Optional[Product]:
        with Session(engine) as session:
            statement = select(Product).where(Product.id == product.id, Product.org == product.org, Product.active == 1)
            results = session.exec(statement)
            db_product = results.first()
            if db_product is None:
                return None
            if db_product.quantity < product.quantity:
                db_product.quantity = -1
                return db_product
            original_quantity = db_product.quantity
            original_rate = db_product.avgBuyRate
            original_used_in_trans =  db_product.usedInTransaction
            current_total_buy_cost = db_product.quantity * db_product.avgBuyRate
            current_total_buy_cost -= product.quantity * db_product.avgBuyRate
            db_product.quantity = round(db_product.quantity - product.quantity, ROUNDING_FACTOR)
            if db_product.quantity == 0:
                db_product.avgBuyRate = 0.0
            else:
                db_product.avgBuyRate = round(current_total_buy_cost/db_product.quantity, ROUNDING_FACTOR)
            db_product.active = 1
            db_product.usedInTransaction = 1
            session.add(db_product)
            session.commit()
            session.refresh(db_product)
            db_product.quantity = original_quantity
            db_product.avgBuyRate = original_rate
            db_product.usedInTransaction = original_used_in_trans
            return db_product
        
    def rollback_quantity(product: Product) -> Optional[Product]:
        with Session(engine) as session:
            statement = select(Product).where(Product.id == product.id, Product.org == product.org, Product.active == 1)
            results = session.exec(statement)
            db_product = results.first()
            if db_product is None:
                return None
            db_product.quantity = round(product.quantity, ROUNDING_FACTOR)
            db_product.avgBuyRate = round(product.avgBuyRate, ROUNDING_FACTOR)
            db_product.active = 1
            db_product.usedInTransaction = product.usedInTransaction
            session.add(db_product)
            session.commit()
            session.refresh(db_product)
            return db_product