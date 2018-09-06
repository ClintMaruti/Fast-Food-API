from flask import request, jsonify, abort, Blueprint

from app.model import orders

orders_ = Blueprint('order',__name__, url_prefix='/api/v1/orders')


@orders_.route('/', methods=['POST'])
def create_order():
    """
    endpoint to create an entry of a specific order
    """
    if not request.json or not 'name' in request.json:
        abort(400)
    order = {
        'id': orders[-1]['id'] + 1,
        'name': request.json['name'],
        'price': request.json['price'],
        'status': request.json['status'],
    }
    orders.append(order)
    return jsonify({'order': order}), 201


@orders_.route('/', methods=['GET'])
def api_all():
    """
    endpoint to Get a list of orders
    """
    return jsonify(orders)


@orders_.route('/<int:order_id>', methods=['GET'])
def api_id(order_id):
    """
    endpoint to Get a list of a specific order
    """
    order = [order for order in orders if order['id'] == order_id]
    if len(order) == 0:
        return "Error: Id not found"
    return jsonify({'order': order[0]})


@orders_.route('/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    """
    endpoint to Update the status of an order.
    """
    order = [order for order in orders if order['id'] == order_id]
    if len(order) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'name' in request.json and not isinstance(request.json['name'], str):
        abort(400)
    if 'price' in request.json and not isinstance(request.json['price'], str):
        abort(400)
    if 'status' in request.json and not isinstance(request.json['status'], bool):
        abort(400)
    order[0]['name'] = request.json.get('name', order[0]['name'])
    order[0]['price'] = request.json.get('price', order[0]['price'])
    order[0]['status'] = request.json.get('status', order[0]['status'])
    return jsonify({'order': order[0]})