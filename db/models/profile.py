from sqlalchemy import Integer, String, Column, Text, ForeignKey
from sqlalchemy.orm import relationship
from db.db_setup import Base
from db.models.associations import profiles_topics_association
from db.models.topic import Topic
#from db.models.user import User


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
    profile_reqs_back = relationship("ProfileReqBack", back_populates='profile')

