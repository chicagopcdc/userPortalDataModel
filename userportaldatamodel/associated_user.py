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


class AssociatedUserRoles(Base):
    __tablename__ = "associated_user_roles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    
    role = Column(String)
    code = Column(String, unique=True)

    create_date = Column(DateTime(timezone=False), server_default=func.now())
    update_date = Column(DateTime(timezone=False), server_default=func.now(), onupdate=func.now())

    def __str__(self):
        str_out = {
            "id": self.id,
            "role": self.role,
            "code": self.code
        }
        return json.dumps(str_out)

    def __repr__(self):
        return self.__str__()


class AssociatedUser(Base):
    __tablename__ = "associated_user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    
    user_id = Column(Integer, nullable=True)
    user_source = Column(String, nullable=True)
    email = Column(Text, nullable=True)

    # Mark intentional relationship overlap to silence SQLAlchemy 2.x SAWarning (no behavior change)
    projects = relationship(
        "Project",
        secondary="project_has_associated_user",
        overlaps="associated_users,associated_users_roles,project_has_associated_user",
    )
    # Mark intentional relationship overlap to silence SQLAlchemy 2.x SAWarning (no behavior change)
    project_role = relationship(
        "ProjectAssociatedUser",
        backref=backref(
            "associated_user_roles",
            overlaps="associated_users,projects",
        ),
        overlaps="associated_users,projects,project_has_associated_user",
    )

    active = Column(Boolean, default=True)
    create_date = Column(DateTime(timezone=False), server_default=func.now())
    update_date = Column(DateTime(timezone=False), server_default=func.now(), onupdate=func.now())

    def __str__(self):
        str_out = {
            "id": self.id,
            "user_id": self.user_id,
            "email": self.email,
            "active": self.active
        }
        return json.dumps(str_out)

    def __repr__(self):
        return self.__str__()


class ProjectAssociatedUser(Base):
    __tablename__ = "project_has_associated_user"

    project_id = Column(Integer, ForeignKey("project.id"), primary_key=True)
    # Mark intentional relationship overlap to silence SQLAlchemy 2.x SAWarning (no behavior change)
    project = relationship(
        "Project",
        backref=backref("project_has_associated_user", overlaps="associated_users,associated_users_roles,projects"),
        overlaps="associated_users,associated_users_roles,projects",
    )

    associated_user_id = Column(Integer, ForeignKey("associated_user.id"), primary_key=True)
    # Mark intentional relationship overlap to silence SQLAlchemy 2.x SAWarning (no behavior change)
    associated_user = relationship(
        "AssociatedUser",
        backref=backref(
            "project_has_associated_user",
            overlaps="associated_users,associated_users_roles,projects,associated_user_roles",
        ),
        overlaps="associated_users,associated_users_roles,projects,associated_user_roles",
    )

    role_id = Column(Integer, ForeignKey('associated_user_roles.id'), nullable=False)
    # Mark intentional relationship overlap to silence SQLAlchemy 2.x SAWarning (no behavior change)
    role = relationship(
        "AssociatedUserRoles",
        backref=backref("project_has_associated_user", overlaps="projects,associated_users,associated_users_roles"),
        overlaps="projects,associated_users,associated_users_roles",
    )

    # METADATA_ACCESS, DATA_ACCESS
    active = Column(Boolean, default=True, nullable=False)
    create_date = Column(DateTime(timezone=False), server_default=func.now())
    update_date = Column(DateTime(timezone=False), server_default=func.now(), onupdate=func.now())





