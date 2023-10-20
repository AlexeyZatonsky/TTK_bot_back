from sqlalchemy import Column, Table, MetaData, String, ForeignKey, UUID, Boolean, Integer
from sqlalchemy.ext.declarative import declarative_base
from ..auth.models import Passport

import uuid


metadata = MetaData()
Base = declarative_base(metadata = metadata)

class Ticket(Base):
    __tablename__ = "Tickets"

    id = Column(Integer, primary_key=True)



ticket_to_pass = Table(
    'ticket_to_pass', 
    metadata,
    Column('ticket_id'), Integer, ForeignKey(Ticket.id),
    Column("pass_id", UUID(as_uuid=True), ForeignKey(Passport.id)))
