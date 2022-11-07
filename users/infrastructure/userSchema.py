from models import User
from config import app

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
    
    id = auto_field()
    name = auto_field()
    typeDocument = auto_field()
    numDocument = auto_field()
    name = auto_field()
    lastName = auto_field()
    hobbie = auto_field()
