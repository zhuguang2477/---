import os
from sqlalchemy import create_engine, text
from backend.app.core.config import settings

def test_connection():
    try:
        print(f"尝试连接数据库: {settings.DATABASE_URL}")
        
        # 创建引擎
        engine = create_engine(settings.DATABASE_URL)
        
        # 测试连接
        with engine.connect() as conn:
            result = conn.execute(text("SELECT version()"))
            version = result.scalar()
            print(f"✅ PostgreSQL 连接成功!")
            print(f"PostgreSQL 版本: {version}")
            
            # 测试数据库列表
            result = conn.execute(text("SELECT datname FROM pg_database WHERE datistemplate = false;"))
            databases = [row[0] for row in result]
            print(f"可用数据库: {databases}")
            
            return True
            
    except Exception as e:
        print(f"❌ 数据库连接失败: {e}")
        return False

if __name__ == "__main__":
    test_connection()
