from core import db
from core.libs import helpers

class Teacher(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.TIMESTAMP(timezone=True), default=helpers.get_utc_now, nullable=False)
    updated_at = db.Column(db.TIMESTAMP(timezone=True), default=helpers.get_utc_now, onupdate=helpers.get_utc_now, nullable=False)

    def __repr__(self):
        return f'<Teacher {self.id}>'

    @classmethod
    def get_all_teachers(cls):
        return cls.query.all()