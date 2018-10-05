from flask_jwt_extended import (jwt_required, get_jwt_identity, create_access_token)
from app.resources.v2.models.model import User
from datetime import datetime, timedelta

credentials = {"name":"Clint",
                "password":"admin123"}

def create_admin_token():
    """Creates admin Token"""
    username = "Clint"
    
    expires = timedelta(minutes=30)  
    token = create_access_token(identity=username, expires_delta=expires)
    return token
