from sqlalchemy import Integer, String, Column, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from db.db_setup import Base
from db.models.associations import profiles_topics_association
from datetime import datetime


class Profile(Base):
    __tablename__ = 'profile'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates='profile', uselist=False)
    quiz_id = Column(Integer, ForeignKey('quiz.id'))
    quiz = relationship("Quiz", back_populates='profile', uselist=False)
    text = Column(Text)
    topics = relationship('Topic', secondary=profiles_topics_association, back_populates='profiles', lazy='selectin')
    last_time_read = Column(DateTime, default=datetime.now)
    # profile_reqs_back = relationship("ProfileReqBack", back_populates='profile')
    # user_reqs = relationship("UserReq", back_populates='profile')
