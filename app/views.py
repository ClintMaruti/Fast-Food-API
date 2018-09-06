from flask import Blueprint

html = Blueprint('views', __name__)


@html.route('/', methods=['GET'])
def home():
    return '''<h1>Fast-Food-Fast APi</h1>
<p>A prototype API for Fast Food Fast app.</p>'''
