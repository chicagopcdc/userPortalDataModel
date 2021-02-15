from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from userportaldatamodel.models import Search


class SearchSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Search

