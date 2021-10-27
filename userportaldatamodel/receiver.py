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


from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class Receiver(Base):
    
    __tablename__ = "receiver"

    id = Column(Integer, primary_key=True, autoincrement=True)
    
    receiver_id = Column(Integer)
    receiver_source = Column(String, default='fence')
    received_at = Column(DateTime(timezone=False), server_default=func.now())

    message_id = Column(Integer, ForeignKey("message.id"))
    message = relationship("Message", backref="receivers")
   

    def __str__(self):
        str_out = {
            "id": self.id,
            "receiver_id": self.receiver_id,
            "received_at": self.received_at,
        }
        return json.dumps(str_out)

    def __repr__(self):
        return self.__str__()



# class ReceiverSchema(SQLAlchemyAutoSchema):
#     class Meta:
#         model = Receiver
