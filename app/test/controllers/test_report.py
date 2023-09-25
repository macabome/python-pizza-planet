# test_report_controller.py

from app.controllers import ReportController  # Import the ReportController class
import pytest

# Define test cases
def test_find_top_costumers():
    # Create test data
    report = [
        {"_id": 1, "client_dni": "123"},
        {"_id": 2, "client_dni": "123"},
        {"_id": 3, "client_dni": "456"},
        {"_id": 4, "client_dni": "789"},
    ]
    controller = ReportController()
    result = controller.find_top_costumers(report)

    assert len(result) == 3 

def test_find_top_ingredient():
    report_list = [
        {"detail": [{"ingredient": {"_id": 1}}, {"ingredient": {"_id": 2}}, {"ingredient": {"_id": 1}}]},
        {"detail": [{"ingredient": {"_id": 2}}, {"ingredient": {"_id": 3}}]},
    ]
    controller = ReportController()
    result = controller.find_top_ingredient(report_list)

    assert result is not None
    assert result["_id"] == 1 

def test_get_most_revenue_month():
    data = [
        {"date": "2023-07-15", "total_price": 100.0},
        {"date": "2023-08-20", "total_price": 150.0},
        {"date": "2023-07-10", "total_price": 200.0},
    ]

    controller = ReportController()
    result = controller.get_most_revenue_month(data)

    assert result == "2023-07"

