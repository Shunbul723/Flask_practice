from flask_app import db

class EmpTab(db.Model):
    id=db.Column(db.Integer ,primary_key=True)
    name=db.Column(db.String(50) ,nullable=False)
    email=db.Column(db.String(50))
    position=db.Column(db.String(50))

