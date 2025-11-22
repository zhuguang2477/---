import redis
from backend.app.core.config import settings

# Redis 客户端实例 - 使用新的 REDIS_URL 属性
redis_client = redis.Redis.from_url(
    settings.REDIS_URL,
    decode_responses=True,  # 自动解码响应
    socket_connect_timeout=5,  # 连接超时
    socket_keepalive=True  # 保持连接
)

def get_redis():
    return redis_client