from persona import Persona

nombre = input("Introduzca el nombre: ")
edad = input("Introduzca la edad: ")
sexo = input("Introduzca el sexo. Por favor, que sea H o M: ")
peso = input("Introduzca el peso: ")
altura = input("Introduzca la altura en cm: ")

persona1 = Persona(nombre,edad,"",sexo,peso,altura)
persona2 = Persona(nombre,edad,"",sexo,peso,)
persona3 = Persona(nombre,edad,"",sexo)
persona4 = Persona()

print(persona1)
print(persona2)
print(persona3)
print(persona4)