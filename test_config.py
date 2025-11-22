#!/usr/bin/env python3
"""
配置验证脚本
运行: python test_config.py
"""

import sys
import os

# 添加项目根目录到 Python 路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from backend.app.core.config import settings
    
    print("✅ 配置加载成功!")
    print(f"📁 项目名称: {settings.PROJECT_NAME}")
    print(f"🔢 版本: {settings.VERSION}")
    print(f"🐘 数据库 URL: {settings.DATABASE_URL}")
    print(f"🔴 Redis URL: {settings.REDIS_URL}")
    print(f"🔑 JWT 密钥: {settings.JWT_SECRET_KEY[:10]}...")  # 只显示前10个字符
    print(f"🌐 CORS 允许的源: {settings.ALLOWED_ORIGINS}")
    print(f"🐛 调试模式: {settings.DEBUG}")
    
except Exception as e:
    print(f"❌ 配置加载失败: {e}")
    sys.exit(1)