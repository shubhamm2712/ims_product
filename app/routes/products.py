from fastapi import APIRouter
from fastapi import Depends, Security

from typing import List, Optional

from ..models.product import Product

from ..service import add_product_service, update_quan_service, del_product_service, get_products_service

from ..utils.auth_validation import VerifyToken
from ..utils.req_body_validation import add_product_validator, del_product_validator, update_quantity_validator
from ..utils.utils import set_org_product

apiRouter = APIRouter()
auth = VerifyToken()

# Product 
@apiRouter.post("/add_product", response_model = List[Product])
async def add_product(product: Product = Depends(add_product_validator), auth_result: dict = Security(auth.verify)) -> List[Product]:
    set_org_product(product, auth_result)
    print("In add_product:",product)
    add_product_service.add_product(product)
    products = await get_product(auth_result)
    return products

@apiRouter.post("/update_prod_quantity", response_model = List[Product])
async def update_prod_quantity(product: Product = Depends(update_quantity_validator), auth_result: dict = Security(auth.verify)) -> List[Product]:
    set_org_product(product, auth_result)
    print("In update_prod_quantity:",product)
    update_quan_service.update_quantity(product)
    products = await get_product(auth_result)
    return products

@apiRouter.post("/del_product", response_model = List[Product])
async def del_product(product: Product = Depends(del_product_validator), auth_result: dict = Security(auth.verify)) -> List[Product]:
    set_org_product(product, auth_result)
    print("In del_product:",product)
    del_product_service.del_product(product)
    products = await get_product(auth_result)
    return products

# Get Products
@apiRouter.get("/get_products", response_model = List[Product])
async def get_product(auth_result: dict = Security(auth.verify)) -> List[Product]:
    product = set_org_product(Product(), auth_result)
    print("In get_products:",product)
    products = get_products_service.get_products(product)
    return products
    # product = Product(**{
    #     "org":"demouser",
    #     "name":"prod1",
    #     "quantity":0.0,
    #     "rate":0.0
    # })
    # return [product]