from ..models.product import Product

from ..exceptions.invalid_body_exceptions import InvalidBodyException

def isProdUpdate(product: Product):
    if product.id:
        return True
    return False

def validateUpdate(product: Product):
    # Check whether id is in db for this org
    pass
    

def add_product(product: Product):
    isUpdate = isProdUpdate(product)
    if isUpdate:
        validateUpdate(product)
        pass
    else:
        pass