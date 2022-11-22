from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "postgresql://flaskuser:123@postgres:5432/flaskdb"
engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
Base = declarative_base()
metadata = Base.metadata

def get_db(): ##forma de gerar valores sobre demanda
    db = Session()
    try:
        yield db
    finally:
        db.close()