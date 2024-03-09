import sys

precios = {
    'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000
}

umbral = int(sys.argv[1])
filtro = sys.argv[2].lower()

def filter():
    if filtro == "mayor" or filtro == "":
        mayor_que = ", ".join(list({k for k , v in precios.items() if v > umbral }))
        print(f"Los productos mayores al umbral son: {mayor_que}")
    elif filtro == "menor":
        menor_que = ", ".join(list({k for k , v in precios.items() if v < umbral }))
        print(f"Los productos menores al umbral son: {menor_que}")
    else:
        print("Lo sentimos, no es una operación válida.")

filter()