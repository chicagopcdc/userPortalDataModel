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




class Transition(Base):
    __tablename__ = "transition"

    id = Column(Integer, primary_key=True, autoincrement=True)
    
    state_src_id = Column(Integer, ForeignKey("state.id"))
    state_src = relationship("State", backref=backref("transition_src"), foreign_keys=[state_src_id])

    state_dst_id = Column(Integer, ForeignKey("state.id"))
    state_dst = relationship("State", backref=backref("transition_dst"), foreign_keys=[state_dst_id])

    create_date = Column(DateTime(timezone=False), server_default=func.now())
    update_date = Column(DateTime(timezone=False), server_default=func.now(), onupdate=func.now())

    def __str__(self):
        str_out = {
            "id": self.id,
            "state_src": self.state_src_id,
            "state_dst": self.state_dst_id
        }
        return json.dumps(str_out)

    def __repr__(self):
        return self.__str__()

