import random
from flask import Flask
from flask.cli import FlaskGroup
from flask_migrate import Migrate
from app.repositories.models import Ingredient, Size, Order, OrderDetail
from app.plugins import db
from app.test.utils.functions import get_random_price, get_random_choice, get_random_string, get_random_phone
import random
from datetime import datetime, timedelta

import os

def date_random():
    init_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31)
    diference = end_date- init_date
    random_date = init_date + timedelta(days=random.randint(0, diference.days))
    return random_date

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)

app = Flask(__name__)
manager = FlaskGroup(app)
migrate = Migrate(app, db)

db.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'python-pizza-planet/pizza.sqlite'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True

ingredients = ["bacon", "tomatoes", "onions", "cheese", "chicken", "beef", "spinach", "corn", "shrimp", "pepperoni", "olives"]
sizes = ["12 inches", "18 inches", "22 inches", "26 inches", "34 inches"]
clients_dni= ["38721654", "59284713", "10973582", "84620197", "45382971", "71893642", "62504819", "93217584", "36489217", "50974368"]
clients_name= ["John Connor", "Sara Connor", "Joe Smith", "Doe Johnson", "Terry Johnson", "Steve Woz", "Tim Cook", "Bill Gates", "Elon Musk", "Jeff Bezos"]


with app.app_context():
    print("Ingreso aca.")
    for ingredient_name in ingredients:
        response= Ingredient.query.all()
        create_ingredient = Ingredient(name=ingredient_name, price=get_random_price(3, 10))
        db.session.add(create_ingredient)
        db.session.commit()
    
    for size_name in sizes:
        create_size = Size(name=size_name, price= get_random_price(6, 30))
        db.session.add(create_size)
        db.session.commit()
    
    
    for _ in range(100):
        j = random.randrange(0,9)
        create_order = Order(
            client_name=clients_name[j], 
            client_dni=clients_dni[j], 
            client_address=get_random_string(), 
            client_phone=get_random_phone(), 
            date= date_random(),
            total_price=get_random_price(20, 60), 
            size_id = random.randint(1, 5)
        )
        db.session.add(create_order)
        db.session.commit()
        for i in range(random.randrange(1,9)):
            total_ingredient = Ingredient.query.count()
            ingredient = Ingredient.query.get(random.randrange(1,total_ingredient))
            orden_detail = OrderDetail(ingredient_id=ingredient._id, order_id=create_order._id, ingredient_price=ingredient.price)
            db.session.add(orden_detail)
            db.session.commit()
    
    print("Database populated successfully!")


