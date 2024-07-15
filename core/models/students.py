# Importing necessary modules from the core package
from core import db
from core.libs import helpers

# Defining the Student model class
class Student(db.Model):
    # Setting the table name for the Student model
    __tablename__ = 'students'
    
    # Defining the columns for the Student table
    id = db.Column(db.Integer, db.Sequence('students_id_seq'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.TIMESTAMP(timezone=True), default=helpers.get_utc_now, nullable=False)
    updated_at = db.Column(db.TIMESTAMP(timezone=True), default=helpers.get_utc_now, onupdate=helpers.get_utc_now, nullable=False)

    # Representation method to display a Student object
    def __repr__(self):
        return f'<Student {self.id}>'