from source.operaciones.operaciones import Operaciones




def main():
    operaciones = Operaciones(3, 2)

    suma = operaciones.sumar()
    resta = operaciones.restar()

    print(resta)


if __name__ == '__main__':
    main()

#demo