from sqlalchemy import Column, MetaData, String, ForeignKey, UUID, Boolean
from sqlalchemy.ext.declarative import declarative_base

import uuid


#добавить инфу id телеграмам

metadata = MetaData()

Base = declarative_base(metadata=metadata)

class User(Base):
    __tablename__ = 'users' 

    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    email = Column(String)
    hashed_password = Column(String(length=1024))
    is_superuser = Column(Boolean, default=False)
    is_verified = Column(Boolean, default=False)


class Passport(Base):
    id = Column(UUID(as_uuid=True), primary_key=True)
    hashed_number = Column(String(length=1024))
    hashed_series = Column(String(length=1024))

class UserData(Base):
    __tablename__ = "user_data"

    id = Column(UUID(as_uuid=True), ForeignKey(User.id), primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    patronymic = Column(String)
    passport = Column(UUID, ForeignKey(Passport.id))


