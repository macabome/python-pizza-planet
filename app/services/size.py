from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, jsonify, request
from .base import BaseService

from ..controllers import SizeController

size = Blueprint('size', __name__)
service_controller = BaseService(SizeController)


@size.route('/', methods=POST)
def create_size():
    return service_controller.create()


@size.route('/', methods=PUT)
def update_size():
    return service_controller.update()


@size.route('/id/<_id>', methods=GET)
def get_size_by_id(_id: int):
    return service_controller.get_by_id(_id)


@size.route('/', methods=GET)
def get_sizes():
    return service_controller.get_all()

