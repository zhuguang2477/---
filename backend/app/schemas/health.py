from pydantic import BaseModel
from typing import Literal, Optional


class HealthCheckResponse(BaseModel):
    """健康检查响应模型"""
    status: Literal["healthy", "unhealthy"]
    database: Optional[Literal["healthy", "unhealthy"]] = None
    redis: Optional[Literal["healthy", "unhealthy"]] = None
    timestamp: str
    version: str

    class Config:
        json_schema_extra = {
            "example": {
                "status": "healthy",
                "database": "healthy", 
                "redis": "healthy",
                "timestamp": "2024-01-01T12:00:00Z",
                "version": "1.0.0"
            }
        }


class DatabaseHealthResponse(BaseModel):
    """数据库健康检查响应模型"""
    database: str = "PostgreSQL"
    status: Literal["connected", "disconnected"]

    class Config:
        json_schema_extra = {
            "example": {
                "database": "PostgreSQL",
                "status": "connected"
            }
        }


class RedisHealthResponse(BaseModel):
    """Redis健康检查响应模型"""
    redis: str = "Redis"
    status: Literal["connected", "disconnected"]

    class Config:
        json_schema_extra = {
            "example": {
                "redis": "Redis", 
                "status": "connected"
            }
        }