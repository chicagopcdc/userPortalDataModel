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




class Request(Base):
    
    __tablename__ = "request"

    # BigInteger
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    # user_id = Column(Integer, nullable=True)

    project_id = Column(Integer, ForeignKey("project.id"))
    project = relationship("Project", backref="requests")

    consortium_data_contributor_id = Column(Integer, ForeignKey("consortium_data_contributor.id"))
    consortium_data_contributor = relationship("ConsortiumDataContributor", backref="requests")
    
    updated_date = Column(DateTime(timezone=False), server_default=func.now(), onupdate=func.now())
    created_date = Column(DateTime(timezone=False), server_default=func.now())
   

    def __str__(self):
        str_out = {
            "id": self.id,
            "user_id": self.user_id
        }
        return json.dumps(str_out)

    def __repr__(self):
        return self.__str__()

