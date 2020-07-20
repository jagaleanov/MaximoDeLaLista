# Escribir un programa que tras asignar números enteros a una lista, 
# determine la posición de la lista en la que se encuentra el máximo valor.
lista = []
maximo=0
posicion=-1
q_numeros=int(input("Cuantos numeros desea ingresar?\n"))
for i in range(1,q_numeros+1):
    print("Ingrese el ",i," numero")
    lista += int(input())

for i in range(1,q_numeros+1):
    if lista[i] > maximo:
        maximo = lista[i]
        posicion= i

print("El máximo de la lista es ",i)