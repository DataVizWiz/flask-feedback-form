from datetime import datetime
from app import db


class Comments(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(120), unique=True, nullable=False)
  comment = db.Column(db.Text, nullable=False)
  date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


  def __repr__(self):
    return f"User('{self.email}', '{self.content}', '{self.date_posted}')"



