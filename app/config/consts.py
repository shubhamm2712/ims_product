## Routes
PATH_PREFIX = "/products"
POST_ADD_PRODUCT = "/add_product"
POST_UPDATE_QUAN = "/update_prod_quantity"
POST_DELETE_PROD = "/del_product"
GET_GET_PRODS = "/get_products"

# Config file
CONFIG_FILE = ".env"

# Logger
LOG_FILE = "app/app.log"

# Databases
DB_FILE_NAME = "app/database/database.db"
DB_ECHO = True

# Service
FLOATING_POINT_ERROR = 10e-4

# EXCEPTIONS
ORG_NOT_FOUND = "Org not found"
ID_NOT_FOUND = "Product ID not found"
QUANTITY_LOW = "Quantity too low to delete"
PRODUCT_DETAILS_MISSING_ADD = "Product details missing in add or update product request"
PRODUCT_DETAILS_MISSING_QUAN = "Product details are missing in update quantity request"
PRODUCT_DETAILS_NEG_QUANTITY = "Product cannot have negative or 0 quantity"
INVALID_PRODUCT_DETAILS_TYPE = "Invalid product details type"

# MODEL
ORG = "org"