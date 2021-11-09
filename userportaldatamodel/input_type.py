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


class InputType(Base):
    __tablename__ = "input_type"

    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String)
    function = Column(String)
    description = Column(String)
    
    create_date = Column(DateTime(timezone=False), server_default=func.now())
    update_date = Column(DateTime(timezone=False), server_default=func.now(), onupdate=func.now())
   

    def __str__(self):
        str_out = {
            "id": self.id,
            "code": self.code,
            "function": self.function,
            "description": self.updated_at
        }
        return json.dumps(str_out)

    def __repr__(self):
        return self.__str__()

