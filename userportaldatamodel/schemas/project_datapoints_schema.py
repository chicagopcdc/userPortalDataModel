from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from userportaldatamodel.models import ProjectDataPoints
from marshmallow_sqlalchemy.fields import Nested
from amanuensis.schema import ProjectSchema

class ProjectDataPointsSchema(SQLAlchemyAutoSchema):
    project = Nested(ProjectSchema)
    
    class Meta:
        model = ProjectDataPoints
        include_fk = True
