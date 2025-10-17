#======================================================
# Proyecto: Gestión de Clientes (Aplicando SOLID)
# Integrantes del grupo:
#   - Sebastian Muñoz
#   - Luna Maria 
#   - Santiago Remolina
# ======================================================

class Cliente:
    def __init__(self, nombre: str, email: str):
        self.nombre = nombre
        self.email = email


class ValidadorEmail:
    def es_valido(self, email: str) -> bool:
        return "@" in email and "." in email


class ValidadorEmailEmpresarial(ValidadorEmail):
    def es_valido(self, email: str) -> bool:
        return super().es_valido(email) and email.endswith("@empresa.com")


class RepositorioCliente:
    def guardar(self, cliente: Cliente):
        print(f" Cliente '{cliente.nombre}' guardado exitosamente en la base de datos.")

    def eliminar(self, cliente: Cliente):
        print(f" Cliente '{cliente.nombre}' eliminado del registro.")


class ServicioCliente:
    def __init__(self, validador: ValidadorEmail, repositorio: RepositorioCliente):
        self.validador = validador
        self.repositorio = repositorio

    def registrar_cliente(self, cliente: Cliente):
        if not self.validador.es_valido(cliente.email):
            raise ValueError(" Email inválido. Registro cancelado.")
        self.repositorio.guardar(cliente)
        print(f" Cliente '{cliente.nombre}' registrado con éxito.")

if __name__ == "__main__":
    print("=== Sistema de Registro de Clientes ===")

    repositorio = RepositorioCliente()
    validador = ValidadorEmailEmpresarial()
    servicio = ServicioCliente(validador, repositorio)

    cliente1 = Cliente("Andrea", "andrea@empresa.com")
    servicio.registrar_cliente(cliente1)