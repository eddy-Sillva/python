import math

def volumenTetaedro():
    while True:
        arista=int(input("Ingrese la logintud de las aristas"))
        if arista>0:
            raiz=math.sqrt(2)
            cuboArista=math.pow(arista,3)
            resultado=(raiz/12)*cuboArista
            return resultado
        else:
            print ("Ingrese una longitud valida")
def volumenEsfera():
    while True:
        radio=int(input("Ingrese el radio de la esfera"))
        if radio>0:
            volumen=(4/3)*3.1416*radio**3
            return volumen
        else:
            print ("Ingrese un radio valida")

def volumenCubo():
    while True:
        lado=int(input("Ingrese el valor del lado del cubo"))
        if lado>0:
            resultadoCubo=math.pow(lado,3)
            return resultadoCubo
        else:
            print ("Ingrese un valor valido")

def volumenPrismaTriangular():
    while True:
        base=int(input("Ingrese la base del triangulo"))
        altura=int(input("Ingrese la altura del triangulo"))
        alturaPrisma=int(input("Ingrese la altura del prima"))
        if base>0 and altura>0 and alturaPrisma>0:
            areaBaseTriangulo=(base*altura)/2
            resultadoVolumenPrima=areaBaseTriangulo*alturaPrisma
            return resultadoVolumenPrima
        else:
            print ("Ingrese un valor valido")
def volumenPrismaRectangular():
    while True:
        area=int(input("Ingrese el area"))
        base=int(input("Ingrese la base"))
        alturaPrisma=int(input("Ingrese la altura"))
        if base>0 and area>0 and alturaPrisma>0:
            resultadoVolumenPrisma=area*base*alturaPrisma
            return resultadoVolumenPrisma
        else:
            print ("Ingrese un valor valido")
def volumenPrismaCuadrangular():
        base=int(input("Ingrese la base"))
        altura=int(input("Ingrese la altura"))
        if base>0 and altura>0:
            baseArea=math.pow(base,2)
            resultadoVolumenPrisma=baseArea*altura
            return resultadoVolumenPrisma
        else:
            print ("Ingrese un valor valido")
def volumenPrismaPentagonal():
    while True:
        lado=int(input("Ingrese el lado"))
        apotema=int(input("Ingrese el apotema"))
        alturaPrisma=int(input("Ingrese la altura"))
        if lado>0 and apotema>0 and alturaPrisma>0:
            perimetro=lado*5
            areaBase=(perimetro*apotema)/2
            resultadoVolumenPrisma=areaBase*alturaPrisma
            return resultadoVolumenPrisma
        else:
            print ("Ingrese un valor valido")

def volumenPrismaHexagonal():
    while True:
        lado=int(input("Ingrese el lado"))
        apotema=int(input("Ingrese el apotema"))
        alturaPrisma=int(input("Ingrese la altura"))
        if lado>0 and apotema>0 and alturaPrisma>0:
            perimetro=lado*6
            areaBase=(perimetro*apotema)/2
            resultadoVolumenPrisma=areaBase*alturaPrisma
            return resultadoVolumenPrisma
        else:
            print ("Ingrese un valor valido")
def volumenPrismaHeptagonal():
    while True:
        lado=int(input("Ingrese el lado"))
        apotema=int(input("Ingrese el apotema"))
        alturaPrisma=int(input("Ingrese la altura"))
        if lado>0 and apotema>0 and alturaPrisma>0:
            perimetro=lado*7
            areaBase=(perimetro*apotema)/2
            resultadoVolumenPrisma=areaBase*alturaPrisma
            return resultadoVolumenPrisma
        else:
            print ("Ingrese un valor valido")

print("Calculadora de volumenes")
while True:
    numero=int(input("1:tetaedro, 2:cubo, 3:prisma triangular, 4:cuadrangular, 5:rectangular, 6:pentagonal, 7:hexagonal, 8:heptagonal, 9:esfera"))
    if numero>0 and numero<10:
        if numero==1:
            print("El volumen del tetaedro apartir de la arista es de: ",volumenTetaedro())
        else:
            if numero==2:
                print("El volumen del cubo es: ",volumenCubo())
            else:
                if numero==9:
                    print("El volumen de la esfera es: ",volumenEsfera())
                else:
                    if numero==3:
                        print("El volumen del prisma triangular es de: ",volumenPrismaTriangular())
                    else:
                        if numero==5:
                            print("El volumen del prisma rectangular es de: ",volumenPrismaRectangular())
                        else:
                            if numero==4:
                                print("El volumen del prisma cuadrangular es de: ",volumenPrismaCuadrangular())
                            else:
                                if numero==6:
                                    print("El volumen del prisma pentagonal es de: ",volumenPrismaPentagonal())
                                else:
                                    if numero==7:
                                        print("El volumen del prisma pentagonal es de: ",volumenPrismaHexagonal())
                                    else:
                                        if numero==8:
                                            print("El volumen del prisma pentagonal es de: ",volumenPrismaHeptagonal())
        break
    else:
        print("Por favor seleccione una opcion valida")


print("Calculadora de indice de masa corporal")
a = float(input ("Su altura en metros por favor: "))
est = a
m = float (input("Su masa en kilogramos por favor :"))
IMC = m / est**2

def indicie(IMC):
    print("IMC: " + str(IMC) )
    if IMC >= 0 and IMC <= 15.99 :
        print ("Delgadez severa")
    elif IMC >= 16.00 and IMC <= 16.99 :
        print ("Delgadez moderada")
    elif IMC >= 17.00 and IMC <= 18.49:
        print ("Delgadez leve")
    elif IMC >= 18.50 and IMC <= 24.99 :
        print ("Normal")
    elif IMC >= 25.00 and IMC <= 29.99:
        print ("Sobrepeso")
    elif IMC >= 30.00 and IMC <= 34.99:
        print ("obesidad leve")
    elif IMC >= 35.00 and IMC <= 39.00:
        print ("obesidad media")
    elif IMC >= 40.00:
        print ("obesidad morbida")
indicie(IMC)