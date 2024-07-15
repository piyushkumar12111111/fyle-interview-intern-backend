from datetime import datetime
from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), default=func.now(), nullable=False, onupdate=func.now())

    def __repr__(self):
        return f'<User {self.username}>'

    @classmethod
    def filter(cls, session, *criterion):
        return session.query(cls).filter(*criterion)

    @classmethod
    def get_by_id(cls, session, _id):
        return cls.filter(session, cls.id == _id).first()

    @classmethod
    def get_by_email(cls, session, email):
        return cls.filter(session, cls.email == email).first()