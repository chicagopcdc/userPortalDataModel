from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested

from userportaldatamodel.models import AttributeListValue


class AttributeListValueSchema(SQLAlchemyAutoSchema):
    input_type = Nested('InputType')

    class Meta:
        model = AttributeListValue
        include_fk = True

