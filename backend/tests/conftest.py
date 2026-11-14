from collections.abc import Generator
from datetime import date

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from app.database import Base, get_db
from app.main import app
from app.models.patient import Patient

from app.models.appointment import Appointment
from app.models.medication import Medication


# Create an in-memory SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)


@pytest.fixture
def db_session() -> Generator[Session, None, None]:
    # Create tables before each test
    Base.metadata.create_all(bind=engine)

    with Session(engine) as session:
        # Insert synthetic test patients
        session.add_all(
            [
                Patient(
                    id=1,
                    first_name="John",
                    last_name="Smith",
                    discharge_date=date(2026, 6, 28),
                    follow_up_status="pending",
                ),
                Patient(
                    id=2,
                    first_name="Jane",
                    last_name="Smith",
                    discharge_date=date(2026, 10, 28),
                    follow_up_status="completed",
                ),
                Patient(
                    id=3,
                    first_name="Adam",
                    last_name="Smith",
                    discharge_date=date(2026, 7, 28),
                    follow_up_status="pending",
                ),
            ]
        )
        session.commit()

        session.add(
            Appointment(
                patient_id=1,
                date=date(2026, 12, 1),
                provider="Dr. Williams",
                reason="Blood pressure follow-up",
                status="scheduled",
            )
        )

        session.commit()

        try:
            yield session
        finally:
            Base.metadata.drop_all(bind=engine)


@pytest.fixture
def client(db_session: Session) -> Generator[TestClient, None, None]:
    # Override FastAPI's database dependency
    def override_get_db() -> Generator[Session, None, None]:
        yield db_session

    app.dependency_overrides[get_db] = override_get_db

    try:
        with TestClient(app) as test_client:
            yield test_client
    finally:
        app.dependency_overrides.clear()