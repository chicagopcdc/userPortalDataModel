from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested

from userportaldatamodel.models import ConsortiumDataContributor


class ConsortiumDataContributorSchema(SQLAlchemyAutoSchema):
    requests = Nested('RequestSchema', many=True)

    class Meta:
        model = ConsortiumDataContributor
        include_fk = True

