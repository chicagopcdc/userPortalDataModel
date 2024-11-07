from . import Base
from sqlalchemy import (
    Integer,
    String,
    Column,
    Boolean,
    DateTime,
)
from sqlalchemy.sql import func

import json

class NotificationLog(Base):
    __tablename__ = "notification_log"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True) 
    message = Column(String, unique=True, nullable=False)
    create_date = Column(DateTime(timezone=False), server_default=func.now(), nullable=False)
    active = Column(Boolean, nullable=False, default=True)

    def __str__(self):
        str_output = {
            "id": self.id,
            "notification": self.notif_message,
            "create_date": self.create_date.isoformat(),
        }
        return json.dumps(str_output)

    def __repr__(self):
        return self.__str__()
