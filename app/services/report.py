from app.common.http_methods import GET, POST
from flask import Blueprint, jsonify, request

from ..controllers import ReportController

report = Blueprint('report', __name__)


@report.route('/', methods=GET)
def get_report():
    order, ingredient, most_revenue, error = ReportController.get_all_orders()
    response = order, ingredient, most_revenue if not error else {'error': error}
    status_code = 200 if order else 404 if not error else 400
    return jsonify(response), status_code
