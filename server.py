# server.py
import logging

from flask import Flask, request, jsonify
from service import InventoryService

app = Flask(__name__)
service = InventoryService()

@app.route('/define_stuff', methods=['POST'])
def define_stuff():
    data = request.json
    type = data.get('type')
    description = data.get('description')
    result = service.define_stuff(type, description)
    return jsonify({'message': result})

@app.route('/undefine', methods=['POST'])
def undefine():
    data = request.json
    type = data.get('type')
    result = service.undefine(type)
    return jsonify({'message': result})

@app.route('/add', methods=['POST'])
def add():
    data = request.json
    quantity = data.get('quantity')
    type = data.get('type')
    result = service.add(quantity, type)
    return jsonify({'message': result})

@app.route('/remove', methods=['POST'])
def remove():
    data = request.json
    quantity = data.get('quantity')
    type = data.get('type')
    result = service.remove(quantity, type)
    return jsonify({'message': result})

@app.route('/get_count', methods=['GET'])
def get_count():
    type = request.args.get('type')  # Get 'type' from query parameters
    result = service.get_count(type)
    if result == -1:
        return jsonify({'message': f"Type '{type}' does not exist."}), 404
    else:
        return jsonify({'type': type, 'count': result})

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    app.run(host='0.0.0.0', port=5000, debug=True)

