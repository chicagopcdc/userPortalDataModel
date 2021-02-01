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


class RequestState(Base):
    __tablename__ = "request_has_state"

    request_id = Column(Integer, ForeignKey("Request.id"), primary_key=True)
    request = relationship("Request", backref=backref("request_has_state"))

    state_id = Column(Integer, ForeignKey("State.id"), primary_key=True)
    state = relationship("State", backref=backref("request_has_state"))

    created_at = Column(DateTime(timezone=False), server_default=func.now())




class State(Base):
    
    __tablename__ = "state"

    # BigInteger
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    name = Column(String)
    code = Column(String)

    created_at = Column(DateTime(timezone=False), server_default=func.now())
   

    def __str__(self):
        str_out = {
            "id": self.id,
            "name": self.name
        }
        return json.dumps(str_out)

    def __repr__(self):
        return self.__str__()

