from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested

from amanuensis.models import Receiver

class ReceiverSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Receiver
