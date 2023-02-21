"""     
        Programa4
        Nombre: Eros YCT
        Fecha: 26/01/2023
        Descripcion: acceso a las variables por posición y nombre
"""
numero1 = 10 # asignamos el valor 10 a numero1
numero2 = 5 # asignamos el valor 5 a numero2
print("{} + {} = {} ".format(numero1 , numero2, numero1 + numero2)) # se imprime la suma y el resultado de la suma de las variables numero1 y numero2 
print("{n1} + {n2} = {suma} ".format(n1=numero1, n2=numero2, suma= numero1 + numero2)) # se imprime la suma y el resultado de las variables
print("{n2} + {n2} = {n2} ".format(n1=numero1, n2=numero2, suma= numero1 + numero2)) # se imprime las variables y el numero 5 ya que ese es el resultado segun el codigo
print("{numero1} + {numero2} = {suma} ".format(numero1=numero1, numero2=numero2, suma= numero1 + numero2)) # se imprime la suma de las dos variables y el resultado de la misma
