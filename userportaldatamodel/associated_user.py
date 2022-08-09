import json

from . import Base

from sqlalchemy import (
    Integer,
    String,
    Column,
    Boolean,
    DateTime,
    Text,
)
from sqlalchemy.sql import func
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship, backref


ASSOCIATED_USER_ROLES = ["DATA_ACCESS", "METADATA_ACCESS"]

class AssociatedUser(Base):
    __tablename__ = "associated_user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    
    user_id = Column(Integer, nullable=True)
    user_source = Column(String, default='fence')
    email = Column(Text, nullable=True)

    # METADATA_ACCESS, DATA_ACCESS
    role = Column(Text, nullable=False)

    projects = relationship("Project", secondary="project_has_associated_user")
    
    active = Column(Boolean, default=True)
    create_date = Column(DateTime(timezone=False), server_default=func.now())
    update_date = Column(DateTime(timezone=False), server_default=func.now(), onupdate=func.now())


    def __str__(self):
        str_out = {
            "id": self.id,
            "user_id": self.user_id,
            "email": self.email,
            "active": self.active,
            "projects": self.projects
        }
        return json.dumps(str_out)

    def __repr__(self):
        return self.__str__()


class ProjectAssociatedUser(Base):
    __tablename__ = "project_has_associated_user"

    project_id = Column(Integer, ForeignKey("project.id"), primary_key=True)
    project = relationship("Project", backref=backref("project_has_associated_user"))

    associated_user_id = Column(Integer, ForeignKey("associated_user.id"), primary_key=True)
    associated_user = relationship("AssociatedUser", backref=backref("project_has_associated_user"))

    create_date = Column(DateTime(timezone=False), server_default=func.now())
    update_date = Column(DateTime(timezone=False), server_default=func.now(), onupdate=func.now())





