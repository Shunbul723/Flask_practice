from flask_app.models import EmpTab
from flask_app import db

def post_controllers(data):
    emp=EmpTab(name=data['name'],email=data['email'],position=data['position'])
    db.session.add(emp)
    db.session.commit()
    return "data inserted"


