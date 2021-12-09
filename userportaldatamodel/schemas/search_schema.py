from enum import Enum

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Enum
from userportaldatamodel.models import FilterSourceType, Search


# class FilterSourceTypeSchema(SQLAlchemyAutoSchema):
#     class Meta:
#         model = FilterSourceType


class SearchSchema(SQLAlchemyAutoSchema):
    filter_source = Enum(FilterSourceType)

    class Meta:
        model = Search
