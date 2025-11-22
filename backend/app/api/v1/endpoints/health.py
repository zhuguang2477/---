from fastapi import APIRouter, Depends
from sqlalchemy import text
from datetime import datetime
import pytz

from backend.app.schemas.health import (
    HealthCheckResponse, 
    DatabaseHealthResponse, 
    RedisHealthResponse
)
from backend.app.database import get_db
from backend.app.redis_client import get_redis
from backend.app.core.config import settings
from sqlalchemy.orm import Session
import redis

router = APIRouter()


def check_database_health(db: Session) -> bool:
    """检查数据库连接状态"""
    try:
        # 执行简单的查询来测试数据库连接
        db.execute(text("SELECT 1"))
        return True
    except Exception as e:
        print(f"Database health check failed: {e}")
        return False


def check_redis_health(redis_client: redis.Redis) -> bool:
    """检查 Redis 连接状态"""
    try:
        return redis_client.ping()
    except Exception as e:
        print(f"Redis health check failed: {e}")
        return False


@router.get(
    "/health",
    response_model=HealthCheckResponse,
    summary="应用健康状态检查",
    description="检查应用、数据库和 Redis 的连接状态"
)
async def health_check(
    db: Session = Depends(get_db),
    redis_client: redis.Redis = Depends(get_redis)
):
    """综合健康检查端点"""
    # 检查数据库连接
    db_healthy = check_database_health(db)
    
    # 检查 Redis 连接
    redis_healthy = check_redis_health(redis_client)
    
    # 确定整体状态
    overall_status = "healthy" if (db_healthy and redis_healthy) else "unhealthy"
    
    # 获取当前时间戳
    current_time = datetime.now(pytz.utc).isoformat()
    
    return HealthCheckResponse(
        status=overall_status,
        database="healthy" if db_healthy else "unhealthy",
        redis="healthy" if redis_healthy else "unhealthy",
        timestamp=current_time,
        version=settings.VERSION
    )


@router.get(
    "/health/database",
    response_model=DatabaseHealthResponse,
    summary="数据库健康检查",
    description="单独检查数据库连接状态"
)
async def database_health_check(db: Session = Depends(get_db)):
    """数据库健康检查端点"""
    is_healthy = check_database_health(db)
    
    return DatabaseHealthResponse(
        status="connected" if is_healthy else "disconnected"
    )


@router.get(
    "/health/redis", 
    response_model=RedisHealthResponse,
    summary="Redis 健康检查",
    description="单独检查 Redis 连接状态"
)
async def redis_health_check(redis_client: redis.Redis = Depends(get_redis)):
    """Redis 健康检查端点"""
    is_healthy = check_redis_health(redis_client)
    
    return RedisHealthResponse(
        status="connected" if is_healthy else "disconnected"
    )