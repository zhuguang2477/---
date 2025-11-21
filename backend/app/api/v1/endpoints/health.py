from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from backend.app.database import get_db
from backend.app.redis_client import get_redis
from backend.app.schemas.health import HealthCheck, DatabaseStatus, RedisStatus
from datetime import datetime

router = APIRouter()

@router.get("/health", response_model=HealthCheck)
async def health_check():
    return HealthCheck(
        status="healthy",
        timestamp=datetime.now()
    )

@router.get("/health/database", response_model=DatabaseStatus)
async def database_health_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        status = "connected"
    except Exception:
        status = "disconnected"
    
    return DatabaseStatus(
        database="PostgreSQL",
        status=status
    )

@router.get("/health/redis", response_model=RedisStatus)
async def redis_health_check(redis=Depends(get_redis)):
    try:
        redis.ping()
        status = "connected"
    except Exception:
        status = "disconnected"
    
    return RedisStatus(
        redis="Redis",
        status=status
    )
