from datetime import datetime
from models import db
from models.users import User

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.Text)
    created_at = db.Column(db.Date, default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey(User.id, ondelete="CASCADE"))
