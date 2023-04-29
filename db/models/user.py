from sqlalchemy import Integer, String, Column, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship
from db.db_setup import Base
from db.models.associations import profiles_topics_association, users_topics_association
from db.models.req import ProfileReq


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
    profile_reqs = relationship("ProfileReq", back_populates='user')
