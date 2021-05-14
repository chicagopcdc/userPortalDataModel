from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested

from userportaldatamodel.models import Request


class RequestSchema(SQLAlchemyAutoSchema):
    messages = Nested('MessageSchema', many=True)
    attributes = Nested('AttributesSchema', many=True)
    project = Nested('ProjectSchema', exclude=["requests"])

    class Meta:
        model = Request
        include_fk = True

