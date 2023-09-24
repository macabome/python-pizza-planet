from sqlalchemy.exc import SQLAlchemyError

from ..common.utils import check_required_keys
from ..repositories.managers import (IngredientManager, OrderManager,
                                     SizeManager, BeverageManager, ReportManager)
from .base import BaseController

from collections import Counter, defaultdict


class ReportController(BaseController):
    manager = ReportManager  

    @staticmethod
    def find_top_costumers(report: list):
        client_dni_counts = {}
        for entry in report:
            client_dni = entry.get("client_dni")
            if client_dni:
                client_dni_counts[client_dni] = client_dni_counts.get(client_dni, 0) + 1

        top_3_most_repeated = [
            client_dni
            for client_dni, count in sorted(client_dni_counts.items(), key=lambda x: x[1], reverse=True)[:3]
        ]

        selected_clients = {}
        added_client_dnies = set() 
        for entry in report:
            client_dni = entry.get("client_dni")
            if client_dni in top_3_most_repeated and client_dni not in added_client_dnies:
                selected_clients[entry["_id"]] = entry
                added_client_dnies.add(client_dni) 

        return selected_clients

    @staticmethod
    def find_top_ingredient(report_list: list):
        all_ingredients = [item.get("ingredient") for report in report_list for item in report.get("detail", [])]
        ingredient_counts = Counter(ingredient["_id"] for ingredient in all_ingredients if ingredient)
        most_common_ingredient_id, most_common_count = ingredient_counts.most_common(1)[0]

        most_common_ingredient_info = None
        for ingredient in all_ingredients:
            if ingredient and ingredient.get("_id") == most_common_ingredient_id:
                most_common_ingredient_info = ingredient
                break

        return most_common_ingredient_info
    
    @staticmethod
    def get_most_revenue_month(data):
        monthly_revenue = defaultdict(float)

        for entry in data:
            revenue = entry.get("total_price", 0.0)
            date = entry.get("date")
            if date:
                year_month = date.split("-")[0:2] 
                month = "-".join(year_month) 
                monthly_revenue[month] += revenue

        max_month = max(monthly_revenue, key=monthly_revenue.get)
        highest_revenue = monthly_revenue[max_month]
        return max_month, highest_revenue

    
    @classmethod
    def get_all_orders(cls):
        try:
            report = OrderManager.get_all()  # Assuming this function returns the report
            error = None  # Initialize error as None, assuming no error occurred
        
        except (SQLAlchemyError, RuntimeError) as ex:
            report = None  # Set report as None in case of an error
            error = str(ex)  # Store the error message as a string

        order = cls.find_top_costumers(report)
        ingredient = cls.find_top_ingredient(report)
        most_revenue = cls.get_most_revenue_month(report)
        return order, ingredient, most_revenue, error  # Return both report and error as a tuple


