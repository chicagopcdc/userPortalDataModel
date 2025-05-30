from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from userportaldatamodel.models import ProjectDataPoints
from marshmallow_sqlalchemy.fields import Nested


class ProjectDataPointsSchema(SQLAlchemyAutoSchema):
    project = Nested('Project')
    
    class Meta:
        model = ProjectDataPoints
        include_fk = True

    
    
