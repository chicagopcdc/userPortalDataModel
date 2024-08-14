from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested

from userportaldatamodel.models import Notification

class NotificationSchema(SQLAlchemyAutoSchema):
    logs = Nested('NotificationLogSchema', many=True) # , exclude=("notification_log",)

    class Meta:
        model = Notification
        include_fk = True