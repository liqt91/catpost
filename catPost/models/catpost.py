from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class UserAuth(Base):
    __tablename__ = 'userAuth'

    aid = Column(Integer, primary_key=True)
    uid = Column(ForeignKey(u'user.uid'), index=True)
    authType = Column(String(45))
    authName = Column(String(45))
    authToken = Column(String(200))

    user = relationship(u'User')

    @property
    def auth_token(self):
        raise AttributeError('auth_token should not be readable.')

    @auth_token.setter
    def auth_token(self,token):
        self.auth_token = generate_password_hash(token)

    def verify_token(self, token):
        check_password_hash(self.auth_token, token)


class User(Base):
    __tablename__ = 'user'

    uid = Column(Integer, primary_key=True)
    username = Column(String(45))
    avator = Column(String(200))



