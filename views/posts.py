from flask import Blueprint, request
from models import db
from models.posts import Post

bp = Blueprint("posts",__name__,url_prefix="/posts")

@bp.route("/", methods=["GET","POST"])
def get_or_create():
    if request.method == "POST":
        request_data = request.get_json()
        post = Post(**request_data)
        db.session.add(post)
        db.session.commit()

    posts =  Post.query.all()
    response = []
    for post in posts:
        response.append({
            "id": post.id,
            "name": post.name,
            "description": post.description,
            "created_at": post.created_at.strftime("%Y-%m-%d"),
            "user_id": post.user_id
        })
    return response


@bp.route('/<int:post_id>',methods=["PUT","GET" ])
def retreive_or_update(post_id):
    post = Post.query.filter_by(id=post_id).first()
    if request.method == "PUT":
        request_data = request.get_json()
        post.name = request_data["name"]
        post.description = request_data["description"]
        db.session.add(post)
        db.session.commit()
    
    return {
            "id": post.id,
            "name": post.name,
            "description": post.description,
            "created_at": post.created_at.strftime("%Y-%m-%d"),
            "user_id": post.user_id,
        }
