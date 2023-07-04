from models import db
from models.posts import Post
from models.users import User

class Comment(db.Model):    
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(120))
    todo_id = db.Column(db.Integer,db.ForeignKey(Post.id, ondelete="CASCADE"))
    user_id = db.Column(db.Integer,db.ForeignKey(User.id, ondelete="CASCADE"))
