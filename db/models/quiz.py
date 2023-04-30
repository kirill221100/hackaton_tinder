from sqlalchemy import Integer, Column, JSON
from sqlalchemy.orm import relationship
from db.db_setup import Base


class Quiz(Base):
    __tablename__ = 'quiz'
    id = Column(Integer, primary_key=True)
    profile = relationship('Profile', back_populates='quiz', uselist=False)
    questions = Column(JSON, nullable=False)
