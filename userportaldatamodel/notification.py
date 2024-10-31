from . import Base
from sqlalchemy import (
    Integer,
    Column,
    Boolean,

)
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey
import json

class Notification(Base):
    __tablename__ = "notification"

    notification_id = Column(Integer, ForeignKey("notification_log.id"), primary_key=True, nullable=False) 
    user_id = Column(Integer, primary_key=True, nullable=False)
    seen = Column(Boolean, nullable=False, default=True)

    notification_log = relationship("NotificationLog", backref="notification")

    def __str__(self):
        str_output = {
            "id": self.notification_id,
            "user": self.user_id,
            "seen": self.seen,
        }
        return json.dumps(str_output)

    def __repr__(self):
        return self.__str__()
