from sqlmodel import Session, SQLModel, create_engine

from app.core.config import settings


engine = create_engine(
    settings.database_url,
    echo=False,
    pool_pre_ping=True,
)

def init_db() -> None:
    """Create all tables. For dev/testing only - use Alembic in prod."""
    SQLModel.metadata.create_all(engine)


def get_session() -> Session:
    """FastAPI dependency that yields a session per request."""
    with Session(engine) as session:
        yield session