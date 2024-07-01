from typing import Optional, Union

from sqlmodel import SQLModel, Field

class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    org: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None
    subtype: Optional[str] = None
    description: Optional[str] = None
    meta_data: Optional[str] = None
    quantity: Optional[float] = None
    rate: Optional[float] = None