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
from marshmallow_sqlalchemy.fields import Nested

class NotificationLog(Base):
    __tablename__ = "notification_log"

    messageid = Column(Integer, primary_key=True, nullable=False, autoincrement=True) 
    message = Column(String)
    create_date = Column(DateTime(timezone=False), server_default=func.now(), nullable=False)
    limit_check = Column(Boolean, nullable=False, server_default='false')

    def __str__(self):
        str_output = {
            "id": self.messageid,
            "message": self.message,
            "create_date": self.create_date,
            "limit_check": self.limit_check,
        }
        return json.dumps(str_output)

    def __repr__(self):
        return self.__str__()

   


