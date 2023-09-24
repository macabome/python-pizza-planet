from datetime import datetime
from app.plugins import db
from app.repositories.models import Order, Ingredient, Beverage, Size, OrderDetail
import random

import pytest
from flask.cli import FlaskGroup
from flask_migrate import Migrate

from app import flask_app

# Define your random data generation functions
def get_random_string(length):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join(random.choice(characters) for _ in range(length))

def get_random_price():
    return round(random.uniform(1.0, 10.0), 2)

# Create a function to populate the database
def populate_database():
    # Create and add 10 Ingredients with random names and prices
    ingredients = []
    for i in range(1, 11):
        ingredient = Ingredient(name=get_random_string(10), price=get_random_price())
        ingredients.append(ingredient)
        db.session.add(ingredient)

    # Create and add 5 Sizes with random names and prices
    sizes = []
    for i in range(1, 6):
        size = Size(name=get_random_string(10), price=get_random_price())
        sizes.append(size)
        db.session.add(size)

    # Create and add 10 Beverages with random names and prices
    beverages = []
    for i in range(1, 11):
        beverage = Beverage(name=get_random_string(10), price=get_random_price())
        beverages.append(beverage)
        db.session.add(beverage)

    # Create and add 100 Orders with OrderDetails
    for i in range(1, 101):
        order = Order(
            client_name=get_random_string(8),
            client_dni=get_random_string(10),
            client_address=get_random_string(20),
            client_phone=get_random_string(12),
            date=datetime.utcnow(),
            total_price=0.0,
            size=random.choice(sizes)
        )

        # Create and add a random number of OrderDetails (between 1 and 5) to each order
        num_order_details = random.randint(1, 5)
        for _ in range(num_order_details):
            ingredient = random.choice(ingredients)
            beverage = random.choice(beverages)
            order_detail = OrderDetail(
                ingredient_price=ingredient.price,
                beverage_price=beverage.price,
                ingredient=ingredient,
                beverage=beverage
            )
            order.order_detail.append(order_detail)

        db.session.add(order)

    # Commit the changes to the database
    db.session.commit()

manager = FlaskGroup(flask_app)

migrate = Migrate()
migrate.init_app(flask_app, db)


if __name__ == '__main__':
    populate_database()


