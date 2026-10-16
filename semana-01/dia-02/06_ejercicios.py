productos = [
    {"nombre": "Laptop", "precio": 2499.99, "stock": 15},
    {"nombre": "Mouse", "precio": 45.50, "stock": 30},
    {"nombre": "Teclado", "precio": 120.00, "stock": 8},
    {"nombre": "Parlante", "precio": 75.00, "stock": 20},
]

# [OK] Mostrar solo los productos con precio menor a S/100
for producto in productos:
    # {"nombre": "Laptop", "precio": 2499.99, "stock": 15},
    if producto["precio"] < 100:
        print(producto["nombre"])

# [OK] Mostrar solo los que tienen stock menor a 10
for producto in productos:
    if producto["stock"] < 10:
        print(f"Producto con poco stock {producto["nombre"]}")

# [OK] Encontrar el producto más caro
mas_caro = productos[0]
for producto in productos:
    if producto["precio"] > mas_caro["precio"]:
        mas_caro = producto
print(f"El producto mas caro {mas_caro["nombre"]}")

# [OK] Crear una lista de nombres de productos con más de 10 unidade
producto_stock = []
for producto in productos:
    if producto["stock"] > 10:
        producto_stock.append(producto["nombre"])
print(producto_stock)  