from fastapi import APIRouter
from fastapi import Depends, Security, Query

from typing import List, Dict

from ..config.consts import PATH_PREFIX, ProductRoutes, ORG
from ..config import logger
from ..exceptions import ExceptionClass
from ..models.product import Product
from ..service import CreateProductService, ReadProductService, UpdateProductService, DeleteProductService
from ..utils import VerifyToken, ProductValidators, set_org_product, set_org_multiple_products

apiRouter = APIRouter(prefix=PATH_PREFIX)
auth = VerifyToken()

bad_request_responses = {
    400: {
        "description": "Error: Bad Request",
        "model": ExceptionClass
    }
}

auth_responses = {
    401: {
        "description": "Error: Unauthorized",
        "model": ExceptionClass
    },
    403: {
        "description": "Error: Forbidden",
        "model": ExceptionClass
    }
}

@apiRouter.post(ProductRoutes.POST_ADD_PRODUCT, response_model=Product, responses=auth_responses|bad_request_responses)
async def add_product(product: Product = Depends(ProductValidators.add_validator), auth_result: Dict = Security(auth.verify)) -> Product:
    set_org_product(product, auth_result)
    logger.debug("In add_product:" + str(product))
    return CreateProductService.add_product(product)

@apiRouter.put(ProductRoutes.PUT_ADD_QUAN_PRODUCT, response_model=Product, responses=auth_responses|bad_request_responses)
async def add_product_quantity(product: Product = Depends(ProductValidators.rate_validator), auth_result: Dict = Security(auth.verify)) -> Product:
    set_org_product(product, auth_result)
    logger.debug("In add_product_quantity:" + str(product))
    return UpdateProductService.add_product_quantity(product)

@apiRouter.put(ProductRoutes.PUT_DEL_QUAN_PRODUCT, response_model=Product, responses=auth_responses|bad_request_responses)
async def del_product_quantity(product: Product = Depends(ProductValidators.quan_validator), auth_result: Dict = Security(auth.verify)) -> Product:
    set_org_product(product, auth_result)
    logger.debug("In del_product_quantity:" + str(product))
    return UpdateProductService.del_product_quantity(product)

@apiRouter.put(ProductRoutes.PUT_ROLLBACK_QUAN_PRODUCT, response_model=Product, responses=auth_responses|bad_request_responses)
async def rollback_product_quantity(product: Product = Depends(ProductValidators.rollback_validator), auth_result: Dict = Security(auth.verify)) -> Product:
    set_org_product(product, auth_result)
    logger.debug("In rollback_product_quantity:" + str(product))
    return UpdateProductService.rollback_product_quantity(product)

@apiRouter.put(ProductRoutes.PUT_DEACTIVATE_PRODUCTS, response_model=List[Product], responses=auth_responses)
async def deactivate_products(products: List[Product] = Depends(ProductValidators.list_id_validator), auth_result: Dict = Security(auth.verify)) -> List[Product]:
    set_org_multiple_products(products, auth_result)
    logger.debug("In deactivate_products:" + str(products))
    UpdateProductService.deactivate_products(products)
    return await get_all_products(auth_result)
    
@apiRouter.put(ProductRoutes.PUT_RECOVER_PRODUCTS, response_model=List[Product], responses=auth_responses)
async def recover_products(products: List[Product] = Depends(ProductValidators.list_id_validator), auth_result: Dict = Security(auth.verify)) -> List[Product]:
    set_org_multiple_products(products, auth_result)
    logger.debug("In recover_products:" + str(products))
    UpdateProductService.recover_products(products)
    return await get_deleted_products(auth_result)

@apiRouter.get(ProductRoutes.GET_PRODUCT+"/{product_id}", response_model=Product, responses=auth_responses|bad_request_responses)
async def get_product(product_id: int, auth_result: Dict = Security(auth.verify)):
    product: Product = Product(id=product_id)
    set_org_product(product, auth_result)
    logger.debug("In get_product:" + str(product))
    return ReadProductService.get_product(product)

@apiRouter.get(ProductRoutes.GET_ALL_PRODUCTS, response_model=List[Product], responses=auth_responses)
async def get_all_products(auth_result: Dict = Security(auth.verify)) -> List[Product]:
    product: Product = set_org_product(Product(), auth_result)
    logger.debug("In get_all_products:" + str(product))
    return ReadProductService.get_all_products(product)

@apiRouter.get(ProductRoutes.GET_PRODUCTS_LIST+"/", response_model=List[Product], responses=auth_responses)
async def get_products_list(product_id: List[int] = Query([]), auth_result: Dict = Security(auth.verify)) -> List[Product]:
    logger.debug("In get_products_list:" + str(product_id))
    return ReadProductService.get_products_list(auth_result[ORG], product_id)

@apiRouter.get(ProductRoutes.GET_DELETED_PRODUCTS, response_model=List[Product], responses=auth_responses)
async def get_deleted_products(auth_result: Dict = Security(auth.verify)) -> List[Product]:
    product: Product = set_org_product(Product(), auth_result)
    logger.debug("In get_deleted_products:" + str(product))
    return ReadProductService.get_deleted_products(product)

@apiRouter.delete(ProductRoutes.DELETE_PRODUCTS, response_model=List[Product], responses=auth_responses)
async def delete_products(products: List[Product] = Depends(ProductValidators.list_id_validator), auth_result: Dict = Security(auth.verify)) -> List[Product]:
    set_org_multiple_products(products, auth_result)
    logger.debug("In delete_products:" + str(products))
    DeleteProductService.delete_products(products)
    return await get_deleted_products(auth_result)