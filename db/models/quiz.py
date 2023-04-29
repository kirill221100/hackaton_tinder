from sqlalchemy import Integer, String, Column, Boolean, ForeignKey, Text, JSON
from sqlalchemy.orm import relationship
from db.db_setup import Base
from db.models.associations import profiles_topics_association, users_topics_association


class Quiz(Base):
    __tablename__ = 'quiz'
    id = Column(Integer, primary_key=True)
    profile = relationship('Profile', back_populates='quiz', uselist=False)
    questions = Column(JSON, nullable=False)
