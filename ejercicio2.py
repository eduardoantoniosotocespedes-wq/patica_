#Ejercicio 2: Clasificación de Postulantes de RRHH (Clase 3)
#Conceptos a evaluar: Operadores lógicos (and, or), condicionales anidados y validación de tipos de datos
#Instrucciones: Diseña un programa para clasificar postulantes laborales en diferentes categorías 
#laborales según su perfil
#Datos a solicitar: Años de experiencia laboral (número entero), nivel de inglés ('A' Avanzado, 'I' Intermedio, 'B' Básico), y si cuenta con
#título universitario ('S' para Sí, 'N' para No)
#Reglas de clasificación
#Senior: Requiere como mínimo 5 años de experiencia, nivel de inglés Avanzado ('A') y contar con Título Universitario ('S').
#Mid-Level: Requiere entre 3 y 4 años de experiencia, y un nivel de inglés Avanzado ('A') o Intermedio ('I'). Poseer título universitario no es un requisito excluyente.
#Junior: Requiere únicamente entre 1 y 2 años de experiencia, sin importar su nivel de inglés o si tiene título.
#No Elegible: Cualquier postulante que tenga menos de 1 año de experiencia o que no cumpla con ninguno de los criterios anteriores.
#Validación: Si el usuario ingresa un número negativo en los años de experiencia, el sistema debe emitir una alerta de error y no realizar 
# la evaluación
print("CLASIFICACION DE POSTULANTES, RESPONDA LAS PREGUNTAS: ")
años= int(input("Ingrese sus años de experiencia laboral: "))
if años <0:
     print("error")
else:     
    ingles= str(input("Ingrese su nivel de ingles(A)avanzado, (B)basico, (I)intermedio ")).upper()
    titulo= str(input("¿Cuenta co titulo universitario?(N)no, (S)yes: ")).upper()
    #senior
    if años >=5:
        if ingles == "A" and titulo == "S":
            print("usted es elegible para senior")
    #mid_level
    elif años >=3 and años <=4:
        if ingles == "A" or ingles == "I" :
                print("usted es elegible para mid_level")   
    #junior
    elif años >=1 and años <=2:
        print("usted es elegible para junior")
    else:
        print("eres una basura ")    