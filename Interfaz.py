def pedir_opcion(mensaje, minimo, maximo):
    while True:
        try:
            opcion = int(input(mensaje))
        except ValueError:
            print("Entrada inválida, ingresá un número")
            continue
        if minimo <= opcion <= maximo:
            return opcion
        print(f"Elegí un número entre {minimo} y {maximo}")
