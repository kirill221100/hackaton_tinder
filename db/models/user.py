from sqlalchemy import Integer, String, Column, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from db.db_setup import Base
from db.models.associations import profiles_topics_association, users_topics_association


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    is_admin = Column(Boolean, default=None)
    username = Column(String, unique=True)
    hashed_password = Column(String)
    profile = relationship('Profile', back_populates='user', uselist=False)
    topics = relationship('Topic', secondary=users_topics_association, back_populates='users')
