from sqlalchemy import Integer, String, Column, Boolean, Text, DateTime
from sqlalchemy.orm import relationship
from db.db_setup import Base
from db.models.associations import users_topics_association
from datetime import datetime


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    is_admin = Column(Boolean, default=None)
    username = Column(String, unique=True)
    hashed_password = Column(String)
    contacts = Column(String)
    about = Column(Text)
    profile = relationship('Profile', back_populates='user', uselist=False)
    topics = relationship('Topic', secondary=users_topics_association, back_populates='users')
    last_time_read = Column(DateTime, default=datetime.now)
