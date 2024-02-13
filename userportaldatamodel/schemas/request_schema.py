from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested

from userportaldatamodel.models import Request


class RequestSchema(SQLAlchemyAutoSchema):
    messages = Nested('MessageSchema', many=True)
    attributes = Nested('AttributesSchema', many=True)
    states = Nested('StateSchema', many=True)
    project = Nested('ProjectSchema', exclude=["requests",])
    consortium_data_contributor = Nested('ConsortiumDataContributorSchema', exclude=["requests",])
    request_has_state = Nested('RequestStateSchema', many=True, exclude=['request'])
    
    class Meta:
        model = Request
        include_fk = True

