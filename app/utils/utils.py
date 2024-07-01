from ..models.product import Product

def set_org_product(product: Product, auth_result: dict):
    product.org = auth_result["org"]
    return product