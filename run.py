import os
from flask import render_template
from app import create_app

config = os.getenv('APP_SETTINGS' or 'default')

app = create_app(config)

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
   