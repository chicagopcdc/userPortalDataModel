from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested

from userportaldatamodel.models import NotificationLog

class NotificationLogSchema(SQLAlchemyAutoSchema):

    class Meta:
        model = NotificationLog
        include_fk = True