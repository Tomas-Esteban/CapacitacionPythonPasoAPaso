print("Ej1-"*40)
#Ej 1: Cree una lista de frutas de 7 elementos, y realice un programa que muestre el tercer elemento de la lista en pantalla.
frutas =["Frutilla","Pera","Ciruela","Kiwi","Banana","Durasno","Uvas"]
print(frutas[3])

print("Ej2-"*40)
#Ej 2: Cree una lista de frutas de 2 elementos, y realice un programa que muestre una oración conteniendo los dos elementos de la lista concatenándolos con texto para formar una oración con sentido.
frutas =["Peras","Bananas"]
print("No podes decir que " + frutas[0] + " son " + frutas[1] + " Porque claramente que " + frutas[1] + " no son " + frutas[0])

print("Ej3-"*40)
#Ej 3: Tome un nombre por consola y presente en la pantalla de la consola la oración.
nombre = input("Ingrese su nombre: ")
print("Hola! " + nombre + " Bienvenido!")

print("Ej4-"*40)
#Ej 4: Tome dos valores por consola, y guarde en una lista: [primer_valor,segundo_valor,la_suma_de_los_valores]
val1 = input("Indique el primer valor: ")
val1 = int(val1)
val2 = input("Indique el segundo valor: ")
val2 = int(val2)
valores = [val1,val2]
sum = sum(valores)
list = [val1 , val2 , sum]
print("Lista " )
print(*list)
