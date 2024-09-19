# IMS Product Microservice

The **Product Microservice** is responsible for managing the product inventory. It allows users to add, update, and delete products — essentially performing CRUD operations. Users can directly manipulate product details like name, type, and description, while the product quantity and its average buy rate are updated only through transactions on the UI. All endpoints in this microservice are secure and require an Auth0 access token for authorization.

## 🚀 Tech Stack

- **Framework**: FastAPI
- **Database**: AWS RDS (PostgreSQL)
- **ORM**: SQLModel (built on top of Pydantic and SQLAlchemy)
- **Authentication**: OAuth2.0 by Auth0

This microservice adheres to industry-standard coding practices, including:

- Use of type annotations throughout the codebase for better readability and type safety.
- Validators are used to parse the input into respective classes and validate the content coming in the requests
- Modular programming and recommended folder structure to reuse the components as much as possible.
- Separation of configuration (e.g., authentication and database credentials) using environment variables for security and flexibility.

## 🛠️ Features

- **CRUD operations** for products.
- **Secure endpoints**: All routes require an Auth0 access token for authentication and authorization.
- **Transaction-based updates**: Product quantity and average buy rate are updated automatically through transactions on the UI.

## Project Structure

- **Root Directory**:
  - `README.md`
  - `.env` (environment file, to be created)
  - `Dockerfile`
  - `requirements.txt`
  - `app/` (Main application folder)
    - `__init__.py`
    - `main.py`
    - `config/`
      - `__init__.py`
      - `config.py`
      - `consts.py`
      - `db_config,py`
      - `logger_config.py`
    - `database/`
      - `__init__.py`
      - `create_product_db.py`
      - `read_product_db.py`
      - `update_product_db.py`
      - `delete_product_db.py`
    - `exceptions/`
      - `__init__.py`
      - `auth_exceptions.py`
      - `invalid_body_exceptions.py`
    - `models/`
      - `__init__.py`
      - `product.py`
    - `routes/`
      - `__init__.py`
      - `products.py`
    - `service/`
      - `__init__.py`
      - `create_product_service.py`
      - `read_product_service.py`
      - `update_product_service.py`
      - `delete_product_service.py`
    - `utils/`
      - `__init__.py`
      - `auth_validation.py`
      - `req_body_validation.py`
      - `utils.py`

## 🔧 Running the Project Locally

### Prerequisites

- Python 3.12
- Postgres database or AWS RDS setup
- Auth0 setup (domain, audience, issuer, and algorithms)

### Step-by-step Instructions

1. **Clone the repository:**

   ```bash
   git clone <your-repo-url>
   cd ims_product
   ```

2. **Install Requirements:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables:** Create a .env file in the root directory with the following details:
   ```makefile
   AUTH0_DOMAIN="<auth0_domain>"
   AUTH0_API_AUDIENCE="<auth0_audience>"
   AUTH0_ISSUER="<auth0_issuer>"
   AUTH0_ALGORITHMS="<algo>"
   ORIGIN="*"
   DB_URL="<DB_URL>"
   ```
