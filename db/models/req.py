from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from db.db_setup import Base


class ProfileReq(Base):
    __tablename__ = 'profile_req'
    id = Column(Integer, primary_key=True)
    profile_id = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='profile_reqs')


class ProfileReqBack(Base):
    __tablename__ = 'profile_req_back'
    id = Column(Integer, primary_key=True)
    profile_id = Column(Integer, ForeignKey('profile.id'))
    profile = relationship('Profile', back_populates='profile_reqs_back')
    user_id = Column(Integer)
    user_contacts = Column(String)
    user_about = Column(String)


class UserReq(Base):
    __tablename__ = 'user_req'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    user_contacts = Column(String)
    user_about = Column(String)
    profile_id = Column(Integer, ForeignKey('profile.id'))
    profile = relationship('Profile', back_populates='user_reqs')
