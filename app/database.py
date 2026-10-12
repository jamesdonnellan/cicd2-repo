from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

DATABASE_URL = "sqlite:///./app.db" # Creates/Uses app.db in the project folder 

engine = create_engine( # SQLAlchemy object that knows how to communicate with the database
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker( # Session factory, creates a new session for a unit of database work
    bind=engine,
    autoflush=False, # Pending changes are not automatically flushed before every query
    expire_on_commit=False, # Objects keep their loaded attribute values after commit, which is convenient when returning them from the endpoint
)

def get_db(): # FastAPI dependency that creates a session, yields it to the endpoint and closes it afterwards
    db = SessionLocal()
    try:
        yield db # yield hands the session to the endpoint
    finally:
        db.close()