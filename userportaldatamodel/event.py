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




class Event(Base):
    __tablename__ = "event"

    id = Column(Integer, primary_key=True, autoincrement=True)
    
    value = Column(String)
    value_required = Column(String)
    is_ec_request = Column(Boolean)

    input_type_id = Column(Integer, ForeignKey("input_type.id"), primary_key=True)
    input_type = relationship("InputType")

    transition_id = Column(Integer, ForeignKey("transition.id"))
    transition = relationship("Transition", backref=backref("events"))

    create_date = Column(DateTime(timezone=False), server_default=func.now())
    update_date = Column(DateTime(timezone=False), server_default=func.now(), onupdate=func.now())
   

    def __str__(self):
        str_out = {
            "id": self.id,
            "name": self.name,
            "input_type": self.input_type_id
        }
        return json.dumps(str_out)

    def __repr__(self):
        return self.__str__()

