from pydantic import BaseModel

from .auth_exception import UnauthenticatedException, UnauthorizedException
from .invalid_body_exceptions import InvalidBodyException

class ExceptionClass(BaseModel):
    detail: str
