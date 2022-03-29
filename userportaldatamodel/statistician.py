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


class ProjectStatistician(Base):
    __tablename__ = "project_has_statistician"

    project_id = Column(Integer, ForeignKey("project.id"), primary_key=True)
    project = relationship("Project", backref=backref("search_in_project"))

    statistician_id = Column(Integer, ForeignKey("statistician.id"), primary_key=True)
    statistician = relationship("Statistician", backref=backref("project_has_statistician"))

    create_date = Column(DateTime(timezone=False), server_default=func.now())
    update_date = Column(DateTime(timezone=False), server_default=func.now(), onupdate=func.now())



class Statistician(Base):
    __tablename__ = "statistician"

    id = Column(Integer, primary_key=True, autoincrement=True)
    
    user_id = Column(Integer, nullable=True)
    user_source = Column(String, default='fence')
    
    email = Column(Text, nullable=True)

    projects = relationship("Project", secondary="project_has_statistician")
    
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
