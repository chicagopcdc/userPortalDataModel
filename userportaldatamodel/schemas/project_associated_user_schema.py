from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from userportaldatamodel.models import ProjectAssociatedUser


class ProjectAssociatedUserSchema(SQLAlchemyAutoSchema):
    associated_users = Nested('AssociatedUserSchema', many=True)

    class Meta:
        model = ProjectAssociatedUser