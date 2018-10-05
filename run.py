import os
from flask import render_template
from app import create_app

config = os.getenv('APP_SETTINGS' or 'default')

app = create_app(config)



@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/swagger.html')
def api():
    return render_template('swagger.html')

if __name__ == "__main__":
    app.run(debug=True)
   