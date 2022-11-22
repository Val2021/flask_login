
from app.adapters.db import Base,engine
from sqlalchemy import Column, String, Integer
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager
from flask import Flask
from flask_login import UserMixin

app = Flask(__name__)
login_manager = LoginManager(app)


class User(Base,UserMixin):
    __tablename__ = "users"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)
    
    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)
    
    def __repr__(self) -> str:
        return f'<User:{self.email}'

Base.metadata.create_all(engine)
