
class PizzaPlace:
    def __init__(self):
        self.observers = []  # Lista de observadores

    def add_observer(self, observer):
        self.observers.append(observer)

    def delete_observer(self, observer):
        self.observers.remove(observer)

    def observers_notify(self, message):
        for observer in self.observers:
            observer.update(message)

    def recieve_order(self, order):
        # Lógica para recibir el pedido
        self.observers_notify(f"New order received: {order}")

    def update_order(self, status, order):
        self.observers_notify(f"New update for {order} with {status}")

class Observer:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"The client {self.name} was notified: {message}")




    