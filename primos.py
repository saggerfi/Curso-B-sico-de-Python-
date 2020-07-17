def run():
    menu = 'Selecciona un número: '
    numero = int(input(menu))
    if primo(numero):
        print(f'El {numero} es primo')
    else:
        print(f'El {numero} no es primo')


def primo(numero):
    if numero == 1:
        return False         
    elif numero == 2:
        return True
    elif numero % 2 == 0:
        return False
    else:
        contador = 0
        for i in range(3, numero + 1):
            if i == 1 or i == numero:
                continue
            if numero % i == 0:
                contador += 1
            if contador == 0:
                return True


if __name__ == '__main__':
    run()