from sqlalchemy import Column, Table, MetaData, String, ForeignKey, UUID, Boolean, Integer, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from ..users.models import Passport

import uuid


metadata = MetaData()
Base = declarative_base(metadata = metadata)

class Train(Base):
    __tablename__ = "Treins"

    id = Column(Integer, primary_key=True)
    trein = Column(String)
    van = Column(String)
    seat = Column(String)
    food_ids = Column(ARRAY(item_type = Integer))



ticket_to_pass = Table(
    'ticket_to_pass', 
    metadata,
    Column('ticket_id'), Integer, ForeignKey(Train.id),
    Column("pass_id", UUID(as_uuid=True), ForeignKey(Passport.id)))
