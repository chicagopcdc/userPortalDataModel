from . import Base
import datetime
from sqlalchemy import (
    Integer,
    String,
    Column,
    Table,
    Boolean,
    BigInteger,
    DateTime,
    Text,
)
from sqlalchemy import UniqueConstraint, Index, CheckConstraint
from sqlalchemy.orm.collections import attribute_mapped_collection
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.dialects.postgresql import ARRAY, JSONB
from sqlalchemy.orm import relationship, backref
from sqlalchemy.schema import ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.types import LargeBinary
from sqlalchemy.orm.collections import MappedCollection, collection
import json




class Message(Base):
    
    __tablename__ = "message"

    # BigInteger
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    sender_id = Column(Integer, nullable=True)
    sent_at = Column(DateTime(timezone=False), server_default=func.now())
    message = Column(String)

    request_id = Column(Integer, ForeignKey("request.id"))
    request = relationship("Request", backref="messages")
   

    def __str__(self):
        str_out = {
            "id": self.id,
            "sender_id": self.sender_id,
            "sent_at": self.sent_at,
            "message": self.message
        }
        return json.dumps(str_out)

    def __repr__(self):
        return self.__str__()

