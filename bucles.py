# contador = 0
# print(f'2 elevado a {contador} es igual a : {2 ** contador}')
# contador = 1
# print(f'2 elevado a {contador} es igual a : {2 ** contador}')
# contador = 2
# print(f'2 elevado a {contador} es igual a : {2 ** contador}')
# contador = 3
# print(f'2 elevado a {contador} es igual a : {2 ** contador}')
# contador = 4
# print(f'2 elevado a {contador} es igual a : {2 ** contador}')
# contador = 5
# print(f'2 elevado a {contador} es igual a : {2 ** contador}')

def run():
    LIMITE = 1000000

    contador = 0
    potencia = 2 ** contador
    while potencia <= LIMITE:
        print(f'2 elevado a {contador} es igual a : {potencia}')
        contador += 1
        potencia = 2 ** contador


if __name__ == '__main__':
    run()