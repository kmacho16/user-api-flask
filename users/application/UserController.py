from config import app, db
from models import User
from flask import jsonify, make_response
from ..infrastructure.schema import UserSchema
import json


@app.route('/users', methods=['GET'])
def index():
    data = User.query.all()
    userSchema = UserSchema(many=True)
    dump_data = userSchema.dump(data)

    print(dump_data)
    return dump_data

def row2dict(row):
    d = {}
    for column in row.columns:
        d[column.name] = str(getattr(row, column.name))

    return d