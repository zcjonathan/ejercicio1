
from re import A


palabra = (input("Ingresa las palabras:"))

def invertir_parentesis (palabra):

    palabra_arreglo= [palabra]
    arreglo = list (palabra)

    ap=-1
    ci=-1

    for i in range(len(arreglo)):
        if arreglo[i] == "(":
            ap=i

        if arreglo[i] == ")":
            ci=i
            break


    rev= reversed(arreglo[ap+1:ci])
    rev=list(rev)

    arreglo=arreglo[:ap]+rev+arreglo[ci+1:]
    palabra= ''.join(arreglo)

    return palabra



print (palabra)

while True:
    if  palabra.find("(") !=-1:
        palabra=invertir_parentesis(palabra)
        print(palabra)
    else:
        break