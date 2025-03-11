products = [
    {"id": 1, "name": "Bujías", "price": 20_000},
    {"id": 2, "name": "Filtros de aire", "price": 30_000},
    {"id": 3, "name": "Pastillas de freno", "price": 70_000},
    {"id": 4, "name": "Amortiguadores", "price": 150_000},
    {"id": 5, "name": "Correas de distribución", "price": 50_000},
    {"id": 6, "name": "Baterías", "price": 150_000},
    {"id": 7, "name": "Cables de encendido", "price": 30_000},
    {"id": 8, "name": "Frenos de disco", "price": 150_000},
    {"id": 9, "name": "Bombas de agua", "price": 100_000},
    {"id": 10, "name": "Radiadores", "price": 200_000},
]

active = True
cart = []

while active:
    print("# Productos disponibles:\n")

    for product in products:
        print(f"* {product['id']}) {product['name']} (COP ${product['price']})")

    id = int(input("\n> ¿Qué producto deseas agregar?: "))

    while id < 1 or id > len(products):
        id = int(input("> Producto inválido, intentalo de nuevo: "))

    for product in products:
        if product["id"] == id:
            record = product

    record["quantity"] = int(input("> ¿Cuántas unidades vas a llevar?: "))

    cart.append(record)

    restart = input("> ¿Deseas agregar otro producto? (s/n): ").lower()

    if restart == "n":
        active = False

    print()  # solo para temas de estilo.

print(cart)
