from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://flask:JZoyvG4eCXOsy2QgQKzgbOhRCHK4hcSz@dpg-cdkl9fsgqg43pc43eu40-a/users_vb61'#'postgresql://flask:JZoyvG4eCXOsy2QgQKzgbOhRCHK4hcSz@dpg-cdkl9fsgqg43pc43eu40-a.oregon-postgres.render.com/users_vb61' #'mysql://flask:flask123@127.0.0.1:8889/users' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
migrate = Migrate(app, db)