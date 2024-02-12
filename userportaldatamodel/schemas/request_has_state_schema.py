from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested
from userportaldatamodel.models import RequestState


class RequestStateSchema(SQLAlchemyAutoSchema):
    state = Nested("StateSchema")
    request = Nested("RequestSchema")
    class Meta:
        model = RequestState
        include_fk = True
        
