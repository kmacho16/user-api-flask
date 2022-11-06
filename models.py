from config import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    typeDocument = db.Column(db.String(50))
    numDocument = db.Column(db.String(80))
    name = db.Column(db.String(200))
    lastaName = db.Column(db.String(200))
    hobbie = db.Column(db.String(200))
