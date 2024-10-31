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

class Notification(Base):
    __tablename__ = "notification"

    notification_id = Column(Integer, ForeignKey("notification_log.id"), primary_key=True, nullable=False) 
    user_id = Column(Integer, ForeignKey("associated_user_roles.id"), primary_key=True, nullable=False)
    seen = Column(Boolean, nullable=False, server_default='false')

    notification_log = relationship("NotificationLog", backref="notification")

    def __str__(self):
        str_output = {
            "id": self.notification_id,
            "user": self.user_id,
            "seen": self.seen,
        }
        return json.dumps(str_output)

    def __repr__(self):
        return self.__str__()
