from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from userportaldatamodel.models import ProjectAssociatedUser


class ProjectAssociatedUserSchema(SQLAlchemyAutoSchema):

    class Meta:
        model = ProjectAssociatedUser