#Ejercicio 3: Taquilla de Cine con match (Clase 4)
#Conceptos a evaluar: Estructuras de selección múltiple (match-case), condiciones anidadas y cálculo de descuentos porcentuales
#Instrucciones: Desarrolla un sistema interactivo para la venta de boletos de un cine
#Utiliza match / case para que el usuario seleccione su tipo de entrada: 1 para Niño, 2 para Adulto, o 3 para Adulto Mayor
#Asigna un precio base según el tipo seleccionado (por ejemplo: Niño: 20 Bs, Adulto: 40 Bs, Adulto Mayor: 15 Bs)
#Pregúntale al usuario el día de la semana actual
#Usando condicionales anidadas, verifica si el día es "miércoles". Si es así, aplica un 20% de descuento sobre la tarifa base
#Imprime el tipo de entrada seleccionado, el descuento aplicado (si corresponde) y el monto total a pagar
print(""" BIENVENIDO A CINEPOLIS, ELIJA SU ENTRADA: 
1.-NIÑO
2.-ADULTO
3.-ADULTO MAYOR""")
option= int(input("Selecciones su tipo de usuario: "))
match option:
    case 1:
        usuario = "niño"
        precio = 20
    case 2:
        usuario = "adulto"
        precio = 40    
    case 3:
        usuario = "adulto mayor"
        precio = 15
    case _:
        print("Usuario invalido")  
if precio > 0:
    dia = input("Ingrese el dia de la samana: ").upper().strip()
    descuento = 0
    if dia == "MIERCOLES":
        descuento = precio * 0.20
        total = precio - descuento
        print(f"Tipo de ussuario: {usuario}")
        print(f"precio: {precio}")
        print(f"total: {total}")
    else:
        print("Opcion invalida")    