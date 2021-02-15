from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested

from userportaldatamodel.models import Message
# from userportaldatamodel.schemas import ReceiverSchema


class MessageSchema(SQLAlchemyAutoSchema):
    receivers = Nested('ReceiverSchema', many=True) # , exclude=("message",)

    class Meta:
        model = Message
        # include_relationships = True
        # load_instance = True
        include_fk = True

