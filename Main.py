#======================================================
# Proyecto: Gestión de Clientes (Aplicando SOLID)
# Integrantes del grupo:
#   - Sebastian Muñoz
#   - Luna Maria 
#   - Santiago Remolina
# ======================================================

if __name__ == "__main__":
    repo = RepositorioCliente()
    servicio = ServicioRegistroCliente(repo)
    cliente1 = Cliente("Andrea", "andrea@empresa.com")
    servicio.registrar_cliente(cliente1)