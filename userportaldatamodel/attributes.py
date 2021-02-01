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




class Attributes(Base):
    
    __tablename__ = "attributes"

    # BigInteger
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    attribute_list_id = Column(Integer, ForeignKey("attribute_list.id"))
    attribute_list = relationship("AttributeList", backref="attribute")

    request_id = Column(Integer, ForeignKey("request.id"))
    request = relationship("Request", backref="messages")

    value = Column(String)

    completed_at = Column(DateTime(timezone=False), server_default=func.now())
   

    def __str__(self):
        str_out = {
            "id": self.id,
            "value": self.value,
            "completed_at": self.completed_at,
        }
        return json.dumps(str_out)

    def __repr__(self):
        return self.__str__()

