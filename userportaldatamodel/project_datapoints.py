from . import Base
from sqlalchemy import (
    Integer,
    String,
    Column,
    CHAR,
)

from sqlalchemy import CheckConstraint
from sqlalchemy.dialects.postgresql import ARRAY
import json

class ProjectDataPoints(Base):
    __tablename__ = "project_datapoints"

    id = Column(Integer,primary_key=True, autoincrement=True)
    term = Column(String)
    value_list = Column(ARRAY(String))
    type = Column(CHAR)
    project_id = Column(Integer)

    __table_args__ = (
         CheckConstraint("datapoints_type IN ('w', 'b')", name="datapoints_type_check"),
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