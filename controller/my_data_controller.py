from flask import Blueprint, request, jsonify
from service.my_data_service import MyDataService

my_data_controller = Blueprint('my_data_controller', __name__)

@my_data_controller.route('/add', methods=['POST'])
def add_data():
    input_data = request.json.get('data')
    result = MyDataService.add_data(input_data)
    return jsonify({"id": result.id, "data": result.data})

