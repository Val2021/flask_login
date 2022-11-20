# from app import db

from app.adapters.db import Base,engine
from sqlalchemy import Column, String, Integer

from werkzeug.security import generate_password_hash, check_password_hash

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(86), nullable=False)
    email = Column(String(86), nullable=False, unique=True)
    password = Column(String(86), nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)
    
    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)

Base.metadata.create_all(engine)
