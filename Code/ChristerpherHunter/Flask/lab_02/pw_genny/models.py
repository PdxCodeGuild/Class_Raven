from pw_genny import db
from datetime import datetime


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    pw_hash = db.Column(db.String(60), unique=True)
    date_made = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"ID: {self.id} @ {self.username}"
