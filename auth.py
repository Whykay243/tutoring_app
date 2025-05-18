from flask import Blueprint
from extensions import db, login_manager

auth = Blueprint('auth', __name__)

# auth routes below...
