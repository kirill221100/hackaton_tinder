from sqlalchemy import Integer, Column, Table, ForeignKey
from db.db_setup import Base

profiles_topics_association = Table('profiles_topics',
                                    Base.metadata,
                                    Column('profile_id', ForeignKey('profile.id'), primary_key=True),
                                    Column('topic_id', ForeignKey('topic.id'), primary_key=True)
                                    )

users_topics_association = Table('users_topics',
                                 Base.metadata,
                                 Column('user_id', ForeignKey('user.id'), primary_key=True),
                                 Column('topic_id', ForeignKey('topic.id'), primary_key=True)
                                 )
