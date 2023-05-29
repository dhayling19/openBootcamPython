import operaciones.operacionesCalculadora


def main():
    resta = operaciones.operacionesCalculadora.resta(7,4)
    print(f'La resta es: {resta}')

    
    suma =  operaciones.operacionesCalculadora.suma(5,6)
    print(f'La suma es: {suma}')

    multiplicacion =  operaciones.operacionesCalculadora.mult(5,6)
    print(f'La multiplicacion es: {multiplicacion}')

    division =  operaciones.operacionesCalculadora.div(5,6)
    print(f'La division es: {division:.2f}')


if __name__ == '__main__':
    main()










