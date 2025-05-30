from . import Base
from sqlalchemy import (
    Integer,
    String,
    Column,
    CHAR,
)

from sqlalchemy import CheckConstraint
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship
import json

class ProjectDataPoints(Base):
    __tablename__ = "project_datapoints"

    id = Column(Integer,primary_key=True, autoincrement=True,nullable=False)
    term = Column(String, nullable = False)
    value_list = Column(ARRAY(String), nullable=False,default=list)
    type = Column(CHAR, nullable=False)

    project_id = Column(Integer,ForeignKey("project.id"),nullable=True)
    project = relationship("Project",backref="project_datapoints")

    __table_args__ = (
         CheckConstraint("type IN ('w', 'b')", name="type_check"),
    )

    def __str__(self):
        str_out = {
            "id": self.id,
            "term": self.term,
            "value_list": self.value_list,
            "type": self.type,
            "project_id": self.project_id
        }
        return json.dumps(str_out)

    def __repr__(self):
            return self.__str__()