
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Complaint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    resolved = db.Column(db.Boolean, default=False)
