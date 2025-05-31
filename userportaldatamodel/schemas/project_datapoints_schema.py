from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from userportaldatamodel.models import ProjectDataPoints
from marshmallow_sqlalchemy.fields import Nested
from amanuensis.schema import ProjectSchema  # Make sure this import is correct

class ProjectDataPointsSchema(SQLAlchemyAutoSchema):
    project = Nested(ProjectSchema)  # Use the actual schema class, not a string
    
    class Meta:
        model = ProjectDataPoints
        include_fk = True
