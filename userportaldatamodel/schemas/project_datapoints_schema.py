from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from userportaldatamodel.models import ProjectDataPoints

"""
created schema for ProjectDataPoints. needs to be updated in the
associated repository.
"""


class ProjectDataPointsSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ProjectDataPoints
        load_instance = True