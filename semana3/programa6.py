"""     
        Programa6
        Nombre: Eros YCT
        Fecha: 31/01/2023
        Descripcion: area y perometro de triangulos
"""
print("Comencemos por el área del triangulo")
base = None
altura = None

while True:
  try:
    base = float(input("Escriba la base del triangulo: "))
    break
  except:
    print("Debe ser un número")

while True:
  try:
    altura = float(input("Escriba la altura del triangulo: "))
    break
  except:
    print("Debe ser un número")

area = base * altura / 2

print("El area del triángulo es: {}".format(area))

print("Ahora pasemos al perímetro del triangulo")

lado1 = float(input("lado1: "))
lado2 = float(input("lado2: "))
lado3 = float(input("lado3: "))
perimetro = lado1 + lado2 + lado3 
print("El perimetro del triangulo es: {} cm".format(perimetro))
