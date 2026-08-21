#Simulación de Cajero Automático (Clase 2)
#Conceptos a evaluar: Bucles de control, contadores de intentos, condicionales y lógica de acceso
#Instrucciones: Diseña un programa que simule el acceso y retiro de dinero en un cajero automático
#Debe solicitar un PIN de seguridad y permitir un máximo de 3 intentos
#Si el PIN ingresado es correcto (define una variable con el PIN real, por ejemplo 1234), dale acceso y solicita el monto que desea retirar
#Verifica que el monto a retirar no supere el saldo disponible inicial de 2000 Bs
#Si el monto es válido, realiza la resta lógica y muestra en pantalla el saldo restante
#Si el usuario falla los 3 intentos de PIN, el programa debe mostrar un mensaje indicando que el acceso ha sido bloqueado
print("CAJERO AUTOMATICO")
pin = 123
intentos = 1
while intentos <= 3:
    pin1 = int(input("Porfavor ingresa pin: ")) 
    if pin1 == pin:
        print("pin correcto:")
        monto = 2000 
        montor= float(input("Ingrese el monto a retirar: "))
        if montor> monto:
            print("Saldo insuficiente...")
            break
        elif montor<1:
            print("caracter erroneo, saliendo...")
            break
        else:
            monto = monto - montor
            print(f"Retiro exitoso, su saldo es de: {monto}bs")   
            break 
    else:
        intentos+=1    
        print("Eduardo estuvo aqui")
