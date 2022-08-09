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




class Project(Base):
    
    __tablename__ = "project"

    # BigInteger
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    name = Column(String, nullable=True)
    first_name = Column(String)
    last_name = Column(String)
    user_id = Column(Integer, nullable=True)
    user_source = Column(String, default='fence')
    #TODO potentially this could be an hubspot ID
    institution = Column(String)
    description = Column(String)

    approved_url = Column(String, nullable=True, default=None)

    active = Column(Boolean, default=True)


    # searches = association_proxy('searches', 'search')
    searches = relationship("Search", secondary="project_has_search")
    statisticians = relationship("Statistician", secondary="project_has_statistician")
    associated_users = relationship("AssociatedUser", secondary="project_has_associated_user")
    associated_users_role = relationship("ProjectAssociatedUser")


    # def __init__(self, **kwargs):
    #     # if "scope" in kwargs:
    #     #     scope = kwargs.pop("scope")
    #     #     if isinstance(scope, list):
    #     #         kwargs["_scope"] = " ".join(scope)
    #     #     else:
    #     #         kwargs["_scope"] = scope
    #     self.id = 1


    update_date = Column(DateTime(timezone=False), server_default=func.now(), onupdate=func.now())
    create_date = Column(DateTime(timezone=False), server_default=func.now())
   

    def __str__(self):
        str_out = {
            "id": self.id,
            "user_id": self.user_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "institution": self.institution,
            "description": self.description,
            "searches": self.searches,
            "statisticians": self.statisticians,
            "associated_users": self.associated_users,
            "approved_url": self.approved_url
        }
        return json.dumps(str_out)

    def __repr__(self):
        return self.__str__()

