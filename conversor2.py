dolares = float(input('¿Cuántos dólares tienes?: '))
valor_pesos = 22.74
pesos = str(round((dolares * valor_pesos), 2))
print(f'Tienes ${pesos} MXN')