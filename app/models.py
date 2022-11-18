from app import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(86), nullable=False)
    email = db.Column(db.String(86), nullable=False, unique=True)
    password = db.Column(db.String(86), nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
