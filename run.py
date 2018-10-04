import os
from flask import redirect
from app import create_app

config = os.getenv('APP_SETTINGS' or 'default')

app = create_app(config)



@app.route('/')
def hello_world():
    return redirect("https://clintmaruti.docs.apiary.io/#")

if __name__ == "__main__":
    app.run(debug=True)
   