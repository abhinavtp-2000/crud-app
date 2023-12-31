from flask import Flask
from models import db
from views.posts import bp
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///post.db"
db.init_app(app)
app.register_blueprint(bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000)