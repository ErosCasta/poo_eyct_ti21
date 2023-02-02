"""     
        Programa6
        Nombre: Eros YCT
        Fecha: 31/01/2023
        Descripcion: area y perometro de triangulos
"""
print("Comencemos por el área del triangulo")
base = None
altura = None

base = float(input("Escriba la base del triangulo: ")) #variable de tipo int o float

altura = float(input("Escriba la altura del triangulo: ")) #variable de tipo int o float
area = base * altura / 2

print("El area del triángulo es: {}".format(area)) #variable de tipo int o float

print("Ahora pasemos al perímetro del triangulo")

lado1 = float(input("lado1: ")) #variable de tipo int o float
lado2 = float(input("lado2: ")) #variable de tipo int o float
lado3 = float(input("lado3: ")) #variable de tipo int o float
perimetro = lado1 + lado2 + lado3 
print("El perimetro del triangulo es: {} cm".format(perimetro)) #variable de tipo int o float
