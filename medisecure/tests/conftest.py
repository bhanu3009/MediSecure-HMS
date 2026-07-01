import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from fastapi.testclient import TestClient

from app.main import app
from app.config.database import Base, get_db

# 1. The RAM Database Setup
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False}, 
    poolclass=StaticPool
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 2. The Override Fixture
@pytest.fixture()
def client():
    # Create all tables in the RAM database right before tests start
    Base.metadata.create_all(bind=engine)

    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    # Swap your real MySQL database for the fake RAM database
    app.dependency_overrides[get_db] = override_get_db

    yield TestClient(app)

    # Destroy the RAM tables instantly after the test finishes
    Base.metadata.drop_all(bind=engine)