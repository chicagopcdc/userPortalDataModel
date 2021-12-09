from enum import Enum

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_enum import EnumField
from userportaldatamodel.models import FilterSourceType, Search


# class FilterSourceTypeSchema(SQLAlchemyAutoSchema):
#     class Meta:
#         model = FilterSourceType


class SearchSchema(SQLAlchemyAutoSchema):
    # filter_source = EnumField(FilterSourceType, by_value=True)

    class Meta:
        model = Search
