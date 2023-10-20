from sqlalchemy import Column, MetaData, String, ForeignKey, UUID, Boolean
from sqlalchemy.ext.declarative import declarative_base

import uuid



users_metadata = MetaData()

Base = declarative_base(metadata=users_metadata)

class User(Base):
    __tablename__ = 'users' 

    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    email = Column(String)
    hashed_password = Column(String(length=1024))
    is_superuser = Column(Boolean, default=False)
    is_verified = Column(Boolean, default=False)

