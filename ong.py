import sys

def factorial(n):
    if n < 0:
        return "no definido"
    elif n == 0 or n == 1:
        return 1
    else:
        fac = 1
        while(n > 1):
            fac *= n
            n -= 1
        return fac
    
def productoria(list):
    elemento = 1
    for num in list:
        elemento = elemento * num
    return elemento
 
def calcular(**kwargs):
    for key, value in kwargs.items():
        if "fact" in key:
            print(f"El factorial de {value} es {factorial(value)}")
        elif "prod" in key:
            print(f"La productoria de {value} es {productoria(value)}")
        else:
            pass

calcular(fact_1 = 5, prod_1 = [3,6,4,2,8], fact_2 = 6)