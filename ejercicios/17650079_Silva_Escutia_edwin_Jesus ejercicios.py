#Un programa que lea dos numeros y nos de la suma
numero1=int(input("Ingresa el primer numero"))
numero2=int(input("Ingresa el segundo numero"))
suma=numero1+numero2
print("El resultado de la suma del numero: ",numero1," Con el numero: ",numero2," Es:",suma)
#programa que pide los datos de registro de una personal
nom=input("ingrese su nombre")
apell=input("ingrese sus apellidos")
direction=input("ingrese su direccion")
postal=input("ingrese su codigo postal")
print("Su nombre es: ",nom," ",apell," Su direccion es: ",direction," Su codigo postal es: ",postal)
#calcular el area de un triangulo
base=input("ingrese la base")
altura=input("ingrese la altura")
resultado=(int(base)*int(altura))/2
print("El area del triaungulo es: ",resultado)
#calcular el volumen de una esfera
radio=int(input("ingresa el radio de la esfera"))
volumen=(4/3)*3.1416*radio**3
print("El volumen de la esfera es: ",volumen)
#dado un numero devolver si es primo o no
primo=int(input("ingrese el numero para saber si es primo o no"))
bandera=True
for a in range(2,primo):
    if primo%a==0:
        bandera=False
        break
if bandera:
    print("El numero: ",primo,"Es primo")
else:
    print("El numero: ",primo,"no es primo")