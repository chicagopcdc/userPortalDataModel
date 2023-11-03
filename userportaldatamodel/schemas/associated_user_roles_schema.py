from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from userportaldatamodel.models import AssociatedUserRoles


class AssociatedUserRolesSchema(SQLAlchemyAutoSchema):

    class Meta:
        model = AssociatedUserRoles