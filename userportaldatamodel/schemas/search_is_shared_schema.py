from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from userportaldatamodel.models import SearchIsShared
from marshmallow_sqlalchemy.fields import Nested


class SearchIsSharedSchema(SQLAlchemyAutoSchema):

    class Meta:
        model = SearchIsShared
        include_fk = True
        search = Nested("SearchSchema")