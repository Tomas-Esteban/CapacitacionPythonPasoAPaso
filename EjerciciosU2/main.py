print("Unidad 2")
print("Ej1")
print("-"*25)
#Escriba un programa que consulte al usuario si desea permanecer en el sitio web y si la respuesta es afirmativa imprimir en pantalla “Bienvenido”, en caso contrario escribir en pantalla “Nos vemos pronto”
response = input("Desea permanecer en el sitio web? 1.Si 2.No ")
if int(reponse) == 1:
    print("Bienvenido!")
else:
    print("Nos vemos pronto!")

print("Ej2")
print("-"*25)
#Escriba un programa que solicite el ingreso de un número y muestre en pantalla si es par o impar.
response = input("Ingrese un numero: ")
if int(response)%2 == 0 or int(response) == 0:
    print("PAR")
else:
    print("INPAR")

print("Ej3")
print("-"*25)
#Escriba un programa que consulte por la edad de la persona e informe:
#Si la persona no está en edad de trabajar.
#Si la persona está en edad de trabajar, con su edad.
#Si la persona está a un año de jubilarse.
response = input("Ingrese su edad por favor!")
if int(response) >= 18 and int(response)<66 and int(response)!=64:
    print("Puede Trabajar")
elif int(response) == 64:
    print("Esta a un año de jubilarse")
else:
    print("No puede trabjar")

response = int(input("Ingrese su edad por favor: "))
counter = 0
edad = counter + 1
listEdad =[]
while edad<response:
    counter=counter+1
    edad=counter
    listEdad.append(edad,)
print(listEdad)
