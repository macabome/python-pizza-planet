from app.common.http_methods import GET, POST
from flask import Blueprint, jsonify, request
from .base import BaseService

from ..controllers import OrderController

order = Blueprint('order', __name__)

service_controller = BaseService(OrderController)


@order.route('/', methods=POST)
def create_order():
    return service_controller.create()


@order.route('/id/<_id>', methods=GET)
def get_order_by_id(_id: int):
    return service_controller.get_by_id(_id)


@order.route('/', methods=GET)
def get_orders():
    return service_controller.get_all()
