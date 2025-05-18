import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    # You can set these as env vars on your EC2 or GitHub Secrets, or hardcode here temporarily
    rds_username = os.getenv("RDS_USERNAME", "admin")
    rds_password = os.getenv("RDS_PASSWORD", "YourStrongPassword123!")
    rds_host = os.getenv("RDS_HOST", "your-rds-endpoint.us-east-1.rds.amazonaws.com")
    rds_port = "3306"
    rds_dbname = os.getenv("RDS_DBNAME", "your_database_name")

    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{rds_username}:{rds_password}@{rds_host}:{rds_port}/{rds_dbname}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)

    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app
