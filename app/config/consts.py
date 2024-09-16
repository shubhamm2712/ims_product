## Routes
PATH_PREFIX = "/products"

# Product Routes
class ProductRoutes:
    POST_ADD_PRODUCT = "/add_product"

    PUT_ADD_QUAN_PRODUCT = "/add_quantity_product"
    PUT_DEL_QUAN_PRODUCT = "/del_quantity_product"

    PUT_ROLLBACK_QUAN_PRODUCT = "/rollback_quantity_product"
    
    PUT_DEACTIVATE_PRODUCTS = "/deactivate_products"
    PUT_RECOVER_PRODUCTS = "/recover_products"

    GET_ALL_PRODUCTS = "/get_all_products"
    GET_PRODUCT = "/get_product"
    GET_PRODUCTS_LIST = "/get_products_list"
    GET_DELETED_PRODUCTS = "/get_deleted_products"

    DELETE_PRODUCTS = "/delete_products"

# Config file
CONFIG_FILE = ".env"

# Logger
LOG_FILE = "app/app.log"

# Databases
DB_ECHO = False
DB_NAME = "imsproduct"

# Service
ROUNDING_FACTOR = 4

# EXCEPTIONS
ORG_NOT_FOUND = "Org not found"
ID_NOT_FOUND = "Product ID not found"
NAME_NOT_FOUND = "Product name not found"
PRODUCT_DOES_NOT_EXIST = "Product does not exist"
QUANTITY_NOT_FOUND = "Quantity not found"
RATE_NOT_FOUND = "Rate not found"
USED_IN_TRANSACTION_NOT_FOUND = "usedInTransaction not found"
PRODUCT_DETAILS_NEG_QUANTITY = "Product does not have enough quantity"
PRODUCT_CANNOT_HAVE_NEG_QUANTITY = "Product cannot have negative quantity"
PRODUCT_CANNOT_HAVE_NEG_OR_ZERO_QUAN = "Product cannot have negative or zero quantity"
PRODUCT_CANNOT_HAVE_NEG_RATE = "Product cannot have negative rate"
INVALID_PRODUCT_DETAILS_TYPE = "Invalid product details type"

# MODEL
ORG = "org"