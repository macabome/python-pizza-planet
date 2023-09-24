from app.common.http_methods import GET, POST
from flask import Blueprint, jsonify, request

from ..controllers import ReportController

report = Blueprint('report', __name__)


@report.route('/', methods=['GET'])
def get_report():
    order, ingredient, most_revenue, error = ReportController.get_all_orders()
    if error:
        response = {'error': error}
        return jsonify(response), 400
    response = {'order': order, 'most_revenue': most_revenue, 'ingredient': ingredient}
    return jsonify(response), 200

