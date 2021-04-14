#Lee por teclado una lista que finalice asta que se ingrese un numero negativo que
print("Primer ejercicio")
lista=[]
while True:
    numero = int(input("Ingrese un numero"))
    if numero>=0:
        lista.append(numero)
    else:
        print("Numero negativo ingresado")
        break
print("La lista de numeros es: ", lista)
# lee N nombres y realizar lo siguiente cuantos nombres se repiten
# y la lista ordenada alfabeticamente
print("Segundo ejercicio")
nombres=[]
while True:
    nombre=input("Ingrese un nombre o ingrese un numero para terminar el llenado")
    if nombre.isalpha():
        nombres.append(nombre)
    else:
        print("Ingresaste un numero")
        break
for i in range(0,len(nombres)):
    if nombres.count(nombres[i])>1:
        print("El nombre:",nombres[i],"Se repite:",nombres.count(nombres[i]),"Veces")
nombres.sort()
print("La lista completa ordenada es:",nombres)

#dada una lista de numeros sumar todos los elementos y dar el resultado
print("Tercer ejercicio")
num=[1,2,3,4,5,6,7,8,9]
resultado=0
for i in range(0,len(num)):
    resultado+=num[i]
print("El resultado de la suma es",resultado)
# realiza la un programa que permita quitar o meter elementos por linea de comando de una lista
print("Cuarto ejercicio")
compra=[]
while True:
    caso=int(input("Ingrese un 1 para agregar, un 2 para quitar o un 0 para salir"))
    if caso==1:
        agregar=input("Agregando un dato al carrito de compra")
        compra.append(agregar)
    else:
        if caso==2:
            quitar=input("Quitando un dato del carrito de compra")
            compra.remove(quitar)
        else:
            if caso==0:
                break

print("La lista final es: ",compra)

#leer una lista de N numeros cuando el usuario decida dejar de insertar numeros mostrar por pantalla se
#cuantos numeros se ingresaron
#cuantos y cuales de ellos son primos devolver una lista aparte
#cuantos de ellos son pares devolver una lista aparte
#cuantos suman todos los elementos del programa
print("Quinto ejercicio")
listaFinal=[]
while True:
    numero=input("Ingrese un numero para agregar a la lista o una letra para terminar el llenado de la lista")
    if numero.isalpha():
        print("Terminando el llenado de la lista")
        break
    else:
        listaFinal.append(int(numero))
print("Se ingresaron un total de: ",len(listaFinal),"Numero(S)")
listaPrimos=[]
listaPares=[]
listaImpares=[]
bandera=True
for i in range(0,len(listaFinal)):
    numero=listaFinal[i]
    if numero%2!=0:
        listaImpares.append(numero)
    else:
        listaPares.append(numero)
    for j in range(2,numero):
        if(numero%j==0):
            bandera=False
            break
    if bandera:
        listaPrimos.append(numero)
    else:
        bandera=True

print("La lista completa es:",listaFinal)
print("La cantidad de numeros primos es: ",len(listaPrimos),"Los cuales son",listaPrimos)
print("La cantidad de numeros pares es: ",len(listaPares),"Los cuales son",listaPares)
print("La cantidad de numeros Impares es: ",len(listaImpares),"Los cuales son",listaImpares)
res=0
for i in range(0,len(listaFinal)):
    res+=listaFinal[i]
print("El resultado de la suma es",res)
