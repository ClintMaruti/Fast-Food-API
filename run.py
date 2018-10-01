import os
from flask_jwt_extended import JWTManager



from app import create_app

config = os.getenv('APP_SETTINGS')

app = create_app(config)

app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
jwt = JWTManager(app)


if __name__ == "__main__":
    app.run(debug=True)
   