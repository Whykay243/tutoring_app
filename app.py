from flask import Flask
from extensions import db, login_manager

def create_app():
    app = Flask(__name__)
    # config...

    db.init_app(app)
    login_manager.init_app(app)

    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app

app = create_app()
