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
    avgBuyRate: Optional[float] = None
    active: Optional[int] = None
    usedInTransaction: Optional[int] = None

    def update(self, product: "Product"):
        self.name = product.name
        self.type = product.type
        self.subtype = product.subtype
        self.description = product.description
        self.metaData = product.metaData