print("TABLA DEL MULTIPLICA HASTA EL 10 DEL NUMERO QUE ELIJAS")
n =  int(input("ingrese un numero"))
for i in range(1,n+1):
    print(f"===TABLA DEL:{i}")
    for j in range(1,11):
        print(f"{j}x{i}= {i*j}")   