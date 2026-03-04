import sys
import os
import uuid
from datetime import datetime, timedelta

import pytest
import jwt
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

# Добавляем путь к корневой папке проекта
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Импортируем из app.config
from app.config import settings
from app.db import db_helper





@pytest.fixture
async def async_session() -> AsyncSession:
    """Фикстура для асинхронной сессии"""
    async with db_helper.session_factory() as session:
        try:
            yield session
        finally:
            await session.rollback()


@pytest.fixture
def mock_user_data():
    """Фикстура с тестовыми данными пользователя"""
    return {
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpass"
    }


@pytest.fixture
def mock_jwt_token():
    """Фикстура для создания тестового JWT токена"""
    data = {"id": str(uuid.uuid4())}
    return jwt.encode(
        data,
        settings.jwt.secret,
        algorithm=settings.jwt.algorithm
    )