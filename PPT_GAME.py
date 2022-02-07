import random



print("MENU IDIOMA")
print("1) Español")
print("2) Ingles")
idioma = int(input("Seleccione su idioma: "))
# 1 
if idioma == 1:
    print("Juego en Español")
    aleatorio = random.randrange(0, 3)
    elijePc = ""
    print("1)Piedra")
    print("2)Papel")
    print("3)Tijera")
    opcion = int(input("Que elijes: "))
    # 2