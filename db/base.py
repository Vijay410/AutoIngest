from typing import Optional
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings


class DatabaseConfig:
    host = "localhost"
    port = 5432
    user = "admin"
    password = "admin"
    database = "StudentInfo"