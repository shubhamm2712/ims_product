from typing import Optional

from sqlmodel import SQLModel, Field

class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    org: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None
    subtype: Optional[str] = None
    description: Optional[str] = None
    metaData: Optional[str] = None
    quantity: Optional[float] = None
    rate: Optional[float] = None

    def update(self, product: "Product"):
        if product.id:
            self.id = product.id
        if product.org:
            self.org = product.org
        if product.name:
            self.name = product.name
        self.type = product.type
        self.subtype = product.subtype
        self.description = product.description
        self.metaData = product.metaData
        if product.quantity:
            self.quantity = product.quantity
        if product.rate:
            self.rate = product.rate