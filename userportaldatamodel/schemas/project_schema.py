from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested

from userportaldatamodel.models import Project


class ProjectSchema(SQLAlchemyAutoSchema):
    searches = Nested('SearchSchema', many=True)
    requests = Nested('RequestSchema', many=True, exclude=["project"])
    statisticians = Nested('StatisticianSchema', many=True)
    associated_users = Nested('AssociatedUserSchema', many=True)
    associated_users_roles = Nested("ProjectAssociatedUserSchema", many=True)


    class Meta:
        model = Project
        include_fk = True

