
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.models.patient import Patient
from scripts.seed_patients import seed_patients


def test_seed_patients_inserts_three_patients(db_session: Session):
    db_session.query(Patient).delete()
    db_session.commit()

    seed_patients(lambda: Session(bind=db_session.connection()))

    count = db_session.scalar(select(func.count()).select_from(Patient))

    assert count == 3


def test_seed_patients_does_not_create_duplicates(db_session: Session):
    seed_patients(lambda: Session(bind=db_session.connection()))
    seed_patients(lambda: Session(bind=db_session.connection()))

    count = db_session.scalar(select(func.count()).select_from(Patient))

    assert count == 3
