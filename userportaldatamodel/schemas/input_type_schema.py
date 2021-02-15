from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from userportaldatamodel.models import InputType


class InputTypeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = InputType

