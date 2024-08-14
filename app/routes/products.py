from fastapi import APIRouter
from fastapi import Depends, Security

from typing import List, Optional

from ..config.consts import PATH_PREFIX, POST_ADD_PRODUCT, POST_UPDATE_QUAN, POST_DELETE_PROD, GET_GET_PRODS, GET_GET_PROD
from ..config.logger_config import logger

from ..models.product import Product

from ..service import add_product_service, update_quan_service, del_product_service, get_products_service

from ..utils.auth_validation import VerifyToken
from ..utils.req_body_validation import add_product_validator, product_validator, update_quantity_validator
from ..utils.utils import set_org_product

apiRouter = APIRouter(prefix=PATH_PREFIX)
auth = VerifyToken()

# Product 
@apiRouter.post(POST_ADD_PRODUCT, response_model = Product)
async def add_product(product: Product = Depends(add_product_validator), auth_result: dict = Security(auth.verify)) -> Product:
    set_org_product(product, auth_result)
    logger.debug("In add_product:" + str(product))
    product = add_product_service.add_product(product)
    return product

@apiRouter.post(POST_UPDATE_QUAN, response_model = Optional[Product])
async def update_prod_quantity(product: Product = Depends(update_quantity_validator), auth_result: dict = Security(auth.verify)) -> Optional[Product]:
    set_org_product(product, auth_result)
    logger.debug("In update_prod_quantity:" + str(product))
    product = update_quan_service.update_quantity(product)
    return product

@apiRouter.post(POST_DELETE_PROD, response_model = List[Product])
async def del_product(product: Product = Depends(product_validator), auth_result: dict = Security(auth.verify)) -> List[Product]:
    set_org_product(product, auth_result)
    logger.debug("In del_product:" + str(product))
    del_product_service.del_product(product)
    products = await get_products(auth_result)
    return products

# Get Products
@apiRouter.get(GET_GET_PRODS, response_model = List[Product])
async def get_products(auth_result: dict = Security(auth.verify)) -> List[Product]:
    product = set_org_product(Product(), auth_result)
    logger.debug("In get_products:" + str(product))
    products = get_products_service.get_products(product)
    return products

@apiRouter.get(GET_GET_PROD, response_model = Product)
async def get_product(product: Product = Depends(product_validator), auth_result: dict = Security(auth.verify)) -> Product:
    set_org_product(product, auth_result)
    logger.debug("In get_products:" + str(product))
    product = get_products_service.get_product(product)
    return Product