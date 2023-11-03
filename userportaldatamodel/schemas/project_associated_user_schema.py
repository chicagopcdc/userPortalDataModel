from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from userportaldatamodel.models import ProjectAssociatedUser
from marshmallow_sqlalchemy.fields import Nested


class ProjectAssociatedUserSchema(SQLAlchemyAutoSchema):
    associated_user = Nested('AssociatedUserSchema')
    role = Nested('AssociatedUserRolesSchema')

    class Meta:
        model = ProjectAssociatedUser