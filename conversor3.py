menu = """
Bienvenido al conversor de monedas ❤

1. Pesos colombianos
2. Pesos argentinos
3. Pesos mexicanos

Elige una opción: """
opcion = int(input(menu))

if opcion == 1:
    pesos = float(input("¿Cuántos pesos colombianos tienes?: "))
    valor_dolar = 3875
    dolares = str(round((pesos / valor_dolar), 2))
    print(f"Tienes ${dolares} dólares")
elif opcion == 2:
    pesos = float(input("¿Cuántos pesos argentinos tienes?: "))
    valor_dolar = 65
    dolares = str(round((pesos / valor_dolar), 2))
    print(f"Tienes ${dolares} dólares")
elif opcion == 3:
    pesos = float(input("¿Cuántos pesos mexicanos tienes?: "))
    valor_dolar = 22.74
    dolares = str(round((pesos / valor_dolar), 2))
    print(f"Tienes ${dolares} dólares")
else:
    print('Introduce una opción valida')
