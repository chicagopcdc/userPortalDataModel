from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested

from userportaldatamodel.models import Attributes


class AttributesSchema(SQLAlchemyAutoSchema):
    attribute_list = Nested('AttributeList')

    class Meta:
        model = Attributes
        include_fk = True

