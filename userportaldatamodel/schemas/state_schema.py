from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from userportaldatamodel.models import State


class StateSchema(SQLAlchemyAutoSchema):

    class Meta:
        model = State

