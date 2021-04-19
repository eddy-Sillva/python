import math
#lambda
sumar=lambda num,num2: num+num2
restar=lambda num,num2: num-num2
multiplicar=lambda num,num2: num*num2
dividir=lambda num,num2: num/num2
elevar=lambda num: num*num
exponente=lambda num,num2: math.pow(num,num2)

print ("Calculadora normal")
while True:
    numero=int(input("1:sumar, 2:restar, 3:multiplicar, 4:dividir, 5:elevar cuadrado, 6:exponente"))
    if numero>0 and numero<7:
        if numero==1:
            num=int(input("Ingrese el primer numero"))
            num2=int(input("Ingrese el segundo numero"))
            print ("El resultado de la suma es: ",sumar(num,num2))
        else:
            if numero==2:
                num=int(input("Ingrese el primer numero"))
                num2=int(input("Ingrese el segundo numero"))
                print ("El resultado de la resta es: ",restar(num,num2))
            else:
                if numero==3:
                    num=int(input("Ingrese el primer numero"))
                    num2=int(input("Ingrese el segundo numero"))
                    print ("El resultado de la multiplicacion es: ",multiplicar(num,num2))
                else:
                    if numero==4:
                        num=int(input("Ingrese el primer numero"))
                        num2=int(input("Ingrese el segundo numero"))
                        print ("El resultado de la division es: ",dividir(num,num2))
                    else:
                        if numero==5:
                            num=int(input("Ingrese el numero para elevarlo al cuadrado"))
                            print ("El resultado de la elevacion al cuadrado es: ",elevar(num))
                        else:
                            if numero==6:
                                num=int(input("Ingrese el primer numero"))
                                num2=int(input("Ingrese el exponente"))
                                print ("El resultado del exponente es",exponente(num,num2))
        break
    else:
        print("Por favor seleccione una opcion valida")

print ("Calculadora de figuras")
areaCuadrado=lambda num: math.pow(num,2)
areaRectangulo= lambda num,num2:num*num2
areaTriangulo=lambda num,num2: (num*num2)/2
areaCirculo=lambda num:math.pi*math.pow(num,2)
areaPentagono=lambda num,num2:(num*num2)/2
while True:
    numero=int(input("1:cuadrado, 2:rectangulo, 3:triangulo, 4:circulo, 5:pentagono"))
    if numero>0 and numero<6:
        if numero==1:
            num=int(input("Ingrese un lado del cuadrado"))
            print ("El del cuadrado es: ",areaCuadrado(num))
        else:
            if numero==2:
                num=int(input("Ingrese la base"))
                num2=int(input("Ingrese la altura"))
                print ("El area del rectangulo es: ",areaRectangulo(num,num2))
            else:
                if numero==3:
                    num=int(input("Ingrese la base"))
                    num2=int(input("Ingrese la altura"))
                    print ("El area del triangulo es: ",areaTriangulo(num,num2))
                else:
                    if numero==4:
                        num=int(input("Ingrese el radio"))
                        print ("El area del circulo es: ",areaCirculo(num))
                    else:
                        if numero==5:
                            num=int(input("Ingrese el perimetro"))
                            num2=int(input("Ingrese el apotema"))
                            print ("El area del pentagono es: ",areaPentagono(num,num2))
        break
    else:
        print("Por favor seleccione una opcion valida")

print ("dado una tupla cuantos numeros son primos")
tupla = (3,5,7,9,10,11,26)
def primo(numero):
    for i in range(2,numero):
        if numero%i==0:
            return False
    return True

print("Un total de: ",len(list(filter(primo,tupla)))," Son primos")
print (list(filter(primo,tupla)))