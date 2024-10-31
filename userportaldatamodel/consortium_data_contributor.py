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


# class ConsortiumDataContributorHasState(Base):
#     __tablename__ = "consortium_data_contributor_has_state"

#     consortium_id = Column(Integer, ForeignKey("consortium_data_contributor.id"), primary_key=True)
#     consortiums = relationship("ConsortiumDataContributor", backref=backref("consortium_data_contributor_has_state"))

#     state_id = Column(Integer, ForeignKey("state.id"), primary_key=True)
#     state = relationship("State", backref=backref("consortium_data_contributor_has_state"))

#     create_date = Column(DateTime(timezone=False), server_default=func.now())
#     update_date = Column(DateTime(timezone=False), server_default=func.now(), onupdate=func.now())


class ConsortiumDataContributor(Base):
    __tablename__ = "consortium_data_contributor"

    # __table_args__ = (
    #     db.UniqueConstraint('component_id', 'commit_id', name='unique_component_commit'),
    # )
    # UniqueConstraint('col2', 'col3', name='uix_1')
    # )

    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String, unique=True)
    name = Column(String)
    
    create_date = Column(DateTime(timezone=False), server_default=func.now())
    update_date = Column(DateTime(timezone=False), server_default=func.now(), onupdate=func.now())
   

    def __str__(self):
        str_out = {
            "id": self.id,
            "name": self.name,
            "code": self.code,
            "update_date": self.update_date.isoformat()
        }
        return json.dumps(str_out)

    def __repr__(self):
        return self.__str__()

