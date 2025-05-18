from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Replace in production

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['UPLOAD_FOLDER'] = 'static/uploads'

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'  # updated for blueprint

# Import and register blueprints
from auth import auth as auth_blueprint
from homework import homework as homework_blueprint

app.register_blueprint(auth_blueprint)
app.register_blueprint(homework_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    db.create_all()
    app.run(host="0.0.0.0", port=80)
