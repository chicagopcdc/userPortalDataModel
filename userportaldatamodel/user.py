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





class User(Base):

    __tablename__ = "User"

    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True)

    # id from identifier, which is not guarenteed to be unique
    # across all identifiers.
    # For most of the cases, it will be same as username
    id_from_idp = Column(String)
    display_name = Column(String)
    phone_number = Column(String)
    email = Column(String)

    _last_auth = Column(DateTime(timezone=False), server_default=func.now())

   
    # groups = association_proxy("user_to_groups", "group")

    active = Column(Boolean)
    is_admin = Column(Boolean, default=False)

    # projects = association_proxy("accesses_privilege", "project")

    # project_access = association_proxy(
    #     "accesses_privilege",
    #     "privilege",
    #     creator=lambda k, v: AccessPrivilege(privilege=v, pj=k),
    # )





    # additional_info = Column(JSONB, server_default=text("'{}'"))

    # def __str__(self):
    #     str_out = {
    #         "id": self.id,
    #         "username": self.username,
    #         "id_from_idp": self.id_from_idp,
    #         "idp_id": self.idp_id,
    #         "department_id": self.department_id,
    #         "active": self.active,
    #         "is_admin": self.is_admin,
    #         "projects": str(self.projects),
    #         "project_access": str(self.project_access),
    #     }
    #     return json.dumps(str_out)

    # def __repr__(self):
    #     return self.__str__()






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