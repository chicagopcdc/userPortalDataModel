from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from userportaldatamodel.models import AssociatedUser


class AssociatedUserSchema(SQLAlchemyAutoSchema):

    class Meta:
        model = AssociatedUser