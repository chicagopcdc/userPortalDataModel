from enum import Enum

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
# from marshmallow_enum import EnumField
# from userportaldatamodel.models import FilterSourceType, Search
from userportaldatamodel.models import Statistician

# Began trying to serialize SearchSchema and FilterSourceType (Enum)
# but ran into difficulties as marshmallow_enum wanted an sqla_session defined
# and I wasn't certain of the impact that would have with other Gen3 apps using
# this package.
# There might be another method for marshmallow enum serializing.
# Left this here for whomever works on it next

class StatisticianSchema(SQLAlchemyAutoSchema):
    # filter_source = EnumField(FilterSourceType, by_value=True)

    class Meta:
        model = Statistician
