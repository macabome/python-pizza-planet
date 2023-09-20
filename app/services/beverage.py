from ..common.http_methods import GET, POST
from flask import Blueprint, jsonify, request

from ..controllers import BeverageController

beverage = Blueprint('beverage', __name__)


@beverage.route('/', methods=POST)
def create_beverage():
    beverage, error = BeverageController.create(request.json)
    response = beverage if not error else {'error': error}
    status_code = 200 if not error else 400
    return jsonify(response), status_code


@beverage.route('/', methods=GET)
def get_beverages():
    beverage, error = BeverageController.get_all()
    response = beverage if not error else {'error': error}
    status_code = 200 if beverage else 404 if not error else 400
    return jsonify(response), status_code