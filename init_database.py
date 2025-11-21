from backend.app.database import engine
from backend.app.models.base import Base

def init_db():
    try:
        # 创建所有表
        Base.metadata.create_all(bind=engine)
        print("✅ 数据库表创建成功!")
        
        # 检查创建的表
        from sqlalchemy import inspect
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        print(f"创建的表: {tables}")
        
    except Exception as e:
        print(f"❌ 数据库表创建失败: {e}")

if __name__ == "__main__":
    init_db()
