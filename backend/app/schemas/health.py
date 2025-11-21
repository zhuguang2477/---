from pydantic import BaseModel
from datetime import datetime

class HealthCheck(BaseModel):
    status: str
    timestamp: datetime
    version: str = "1.0.0"

class DatabaseStatus(BaseModel):
    database: str
    status: str

class RedisStatus(BaseModel):
    redis: str
    status: str
