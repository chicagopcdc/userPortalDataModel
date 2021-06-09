from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested

from userportaldatamodel.models import AttributeList


class AttributeListSchema(SQLAlchemyAutoSchema):
    input_type = Nested('InputType')
    values = Nested('AttributeListValue', many=True)

    class Meta:
        model = AttributeList
        include_fk = True

