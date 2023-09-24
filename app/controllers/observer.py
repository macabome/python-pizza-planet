
class PizzaPlace:
    def __init__(self):
        self.observadores = []  # Lista de observadores

    def agregar_observador(self, observador):
        self.observadores.append(observador)

    def eliminar_observador(self, observador):
        self.observadores.remove(observador)

    def notificar_observadores(self, mensaje):
        for observador in self.observadores:
            observador.actualizar(mensaje)

    def recibir_pedido(self, pedido):
        # Lógica para recibir el pedido
        self.notificar_observadores(f"Nuevo pedido recibido: {pedido}")

    def actualizar(self, message, name):
        print(f"Cliente {name} ha sido notificado: {message}")


if __name__ == "__main__":
    pizzeria = PizzaPlace()

    # Cuando generas una orden --- Tienes el cliente...
    pizzeria.agregar_observador(Client)

    pizzeria.recibir_pedido(Order)

    pizzeria.actualizar(self, message, client.name)


    pizzeria.eliminar_observador(Client)

    