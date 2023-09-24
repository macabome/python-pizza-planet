from sqlalchemy.exc import SQLAlchemyError

from ..common.utils import check_required_keys
from ..repositories.managers import (IngredientManager, OrderManager,
                                     SizeManager, BeverageManager)
from .base import BaseController
from .publisher import PizzaPlace, Observer


class OrderController(BaseController):
    manager = OrderManager
    __required_info = ('client_name', 'client_dni', 'client_address', 'client_phone', 'size_id')
    pizza_order = PizzaPlace()

    @staticmethod
    def calculate_order_price(size_price: float, ingredients: list, beverages: list):
        ingredient_price = sum(ingredient.price for ingredient in ingredients)
        beverage_price = sum(beverage.price for beverage in beverages)
        price = ingredient_price + beverage_price + size_price
        return round(price, 2)


    @classmethod
    def create(cls, order: dict):
        current_order = order.copy()
        if not check_required_keys(cls.__required_info, current_order):
            return 'Invalid order payload', None

        size_id = current_order.get('size_id')
        size = SizeManager.get_by_id(size_id)
        

        if not size:
            return 'Invalid size for Order', None
        

        ingredient_ids = current_order.pop('ingredients', [])
        beverage_ids = current_order.pop('beverages', [])
        print("holiwis-----------------------")
        try:
            beverages = BeverageManager.get_by_id_list(beverage_ids)
            print("------------beverages------------")
            print(beverages)
            ingredients = IngredientManager.get_by_id_list(ingredient_ids)
            print("----- im here-------")
            price = cls.calculate_order_price(size.get('price'), ingredients, beverages)
            order_state = "Received"
            print(order_state)
            order_with_price = {**current_order, 'total_price': price, "order_status": order_state}
            print(order_state)
            created_order = cls.manager.create(order_with_price, ingredients, beverages), None
            print("----------Created order----------")
            print(created_order)
            order_info, _ = created_order
            order_id = order_info["_id"]  
            client_name = order_info["client_name"]  

            cls.create_observer(order_id, client_name)
            return created_order
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)
    
    @classmethod
    def create_observer(cls, order_id, client_name):
        observer = Observer(client_name)
        cls.pizza_order.add_observer(observer)
        cls.pizza_order.recieve_order(order_id)
    
    @classmethod
    def update_state(cls, order_id, status):
        try:
            cls.pizza_order.update_order(status, order_id)
            return cls.manager.update_status(order_id, status), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)
