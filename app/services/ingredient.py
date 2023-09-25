from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, jsonify, request
from .base import BaseService

from ..controllers import IngredientController

ingredient = Blueprint('ingredient', __name__)
service_controller = BaseService(IngredientController)


@ingredient.route('/', methods=POST)
def create_ingredient():
    return service_controller.create()


@ingredient.route('/', methods=PUT)
def update_ingredient():
    return service_controller.update()


@ingredient.route('/id/<_id>', methods=GET)
def get_ingredient_by_id(_id: int):
    return service_controller.get_by_id(_id)


@ingredient.route('/', methods=GET)
def get_ingredients():
    return service_controller.get_all()
