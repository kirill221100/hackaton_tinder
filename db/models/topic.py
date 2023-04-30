from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship
from db.db_setup import Base
from db.models.associations import profiles_topics_association, users_topics_association


class Topic(Base):
    __tablename__ = 'topic'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    profiles = relationship('Profile', secondary=profiles_topics_association, back_populates='topics')
    users = relationship('User', secondary=users_topics_association, back_populates='topics')
