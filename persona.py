import random


class Persona:

    def __init__(self, nombre="", edad=0, dni="", sexo="M", peso=0, altura=0):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        self.sexo = sexo
        self.peso = peso
        self.altura = altura

    def __str__(self):
        return "Nombre: " + str(self.nombre) + " Edad= " + str(self.edad) + " DNI= " + str(self.dni) + " Sexo: " + str(
            self.sexo) + " Peso= " + str(self.peso) + " Altura= " + str(self.altura)

    def calculoIMC(self):
        imc = self.peso / (self.altura ** 2)
        if imc < 0:
            print(-1)
        elif imc == 0:
            print(0)
        else:
            print(1)

    def mayorDeEdad(self):
        if self.edad < 18:
            return False
        else:
            return True

    def meterSexo(self):
        numero = random.randrange(10000000, 99999999)
        letraDni = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L",
                    "C", "K", "E"]
        letra = letraDni[numero % 23]
        self.dni = repr(numero) + letra

