a = ["ensamblaje","ingles" ]
b = ["desarrollo personal", "telematica"]
c = ["programacion","telematica"]
d = ["sistemas operativos", ]
e = ["programacion", "diseño grafico"]
semana = {
    "lunes":a,
    "martes":b,
    "miercoles":c,
    "jueves":d,
    "viernes":e
    }
for dias,horario in semana.items():
    print(f"--horarios de dia {dias}---")
    for dia in horario:
        print(dia)