from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash
from app.models import db, User
from app.utils import hash_password

def create_user(username, password):
    hashed_password = hash_password(password)
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

def verify_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        return create_access_token(identity=user.id)
    return None
