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
    text,
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





class Search(Base):
    
    __tablename__ = "search"

    id = Column(Integer, primary_key=True, autoincrement=True)
    
    user_id = Column(Integer, nullable=True)
    user_source = Column(String)
    
    name = Column(String, nullable=True)
    description = Column(String, nullable=True)
    filter_object = Column(JSONB, server_default=text("'{}'"))
    ids_list = Column(String, nullable=True)

    es_index = Column(String(255))
    dataset_version = Column(String(255))

    is_superseded_by = Column(Integer, default=None)
    active = Column(Boolean, default=True)

    update_date = Column(DateTime(timezone=False), server_default=func.now(), onupdate=func.now())
    create_date = Column(DateTime(timezone=False), server_default=func.now())

    # def __init__(self, **kwargs):
    #     # if "scope" in kwargs:
    #     #     scope = kwargs.pop("scope")
    #     #     if isinstance(scope, list):
    #     #         kwargs["_scope"] = " ".join(scope)
    #     #     else:
    #     #         kwargs["_scope"] = scope
    #     self.id = 1

    def __str__(self):
        str_out = {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "filter_object": self.filter_object,
        }
        return json.dumps(str_out)

    def __repr__(self):
        return self.__str__()






# class UserToBucket(Base):
#     """Unused"""

#     __tablename__ = "user_to_bucket"

#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey(User.id, ondelete="CASCADE"))
#     user = relationship(
#         User,
#         backref=backref(
#             "user_to_buckets", cascade="all, delete-orphan", passive_deletes=True
#         ),
#     )

#     bucket_id = Column(Integer, ForeignKey("bucket.id", ondelete="CASCADE"))
#     bucket = relationship(
#         "Bucket",
#         backref=backref(
#             "user_to_buckets", cascade="all, delete-orphan", passive_deletes=True
#         ),
#     )
#     privilege = Column(ARRAY(String))


# class Bucket(Base):
#     __tablename__ = "bucket"

#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     provider_id = Column(Integer, ForeignKey("cloud_provider.id", ondelete="CASCADE"))
#     provider = relationship(
#         "CloudProvider",
#         backref=backref("buckets", cascade="all, delete-orphan", passive_deletes=True),
#     )
#     users = association_proxy("user_to_buckets", "user")





#     # def __str__(self):
#     #     str_out = {
#     #         "id": self.id,
#     #         "name": self.name,
#     #         "auth_id": self.auth_id,
#     #         "description": self.description,
#     #         "parent_id": self.parent_id,
#     #     }
#     #     return json.dumps(str_out)

#     # def __repr__(self):
#     #     return self.__str__()



    
#     # backref=backref(
#     #         "project_to_buckets", cascade="all, delete-orphan", passive_deletes=True
#     #     ),
#     # privilege = Column(ARRAY(String))
#     # additional_info = Column(JSONB)



# class S3Credential(Base):
#     __tablename__ = "s3credential"

#     id = Column(Integer, primary_key=True)
#         # org_id = Column(Integer, ForeignKey("organization.id"))
#         # application_id = Column(Integer, ForeignKey("application.id", ondelete="CASCADE"))
#     user_id = Column(Integer, ForeignKey(User.id, ondelete="CASCADE"))
#     user = relationship(
#         "User",
#         backref=backref(
#             "s3credentials", cascade="all, delete-orphan", passive_deletes=True
#         ),
#     )

#     access_key = Column(String)

#     timestamp = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
#     expire = Column(Integer)
#     name = Column(String(40))
#     extension = Column(String)

#     @property
#     def filename(self):
#         return "{}.{}".format(self.name, self.extension)


# class Tag(Base):
#     __tablename__ = "tag"

#     user_id = Column(Integer, ForeignKey(User.id, ondelete="CASCADE"), primary_key=True)
#     key = Column(String, primary_key=True)
#     value = Column(String)
#     user = relationship(
#         "User",
#         backref=backref("tags", cascade="all, delete-orphan", passive_deletes=True),
#     )