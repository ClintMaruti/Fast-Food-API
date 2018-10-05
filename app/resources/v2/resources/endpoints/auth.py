import jwt
from functools import wraps
from flask import request, jsonify, make_response
import os


key = os.getenv('SECRET_KEY')
def token_required(function):
    @wraps(function)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message' : 'Token is requied'})

        try:
            data = jwt.decode(token, key)
        except:
            return jsonify({'Message: ': 'Token is invalid!'})

        return function(*args, **kwargs)
    return decorated