from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested
from userportaldatamodel.models import FilterSourceType, Search


class FilterSourceType(SQLAlchemyAutoSchema):
    class Meta:
        model = FilterSourceType


class SearchSchema(SQLAlchemyAutoSchema):
    filter_source = Nested('FilterSourceType')

    class Meta:
        model = Search
