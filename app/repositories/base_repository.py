from app.models import Base


class BaseRepository:
    def __init__(self, session, model):
        self.session = session
        self.model = model

    def get_by_id(self, id: int):
            return self.session.query(self.model).filter_by(id=id).first()
    
    def get_login_email(self, email: str):
        return self.session.query(self.model).filter_by(email=email).first()