from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, jsonify, request
from .base import BaseService

from ..controllers import BeverageController

beverage = Blueprint('beverage', __name__)
service_controller = BaseService(BeverageController)

@beverage.route('/', methods=POST)
def create_beverage():
    return service_controller.create()


@beverage.route('/', methods=GET)
def get_beverages():
    return service_controller.get_all()

@beverage.route('/id/<_id>', methods=GET)
def get_beverage_by_id(_id: int):
    return service_controller.get_by_id(_id)