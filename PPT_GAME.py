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
    if opcion == 1:
        elijeUsuario = "piedra"
    elif opcion == 2:
        elijeUsuario = "papel"
    elif opcion == 3:
        elijeUsuario = "tijera"
    print("Tu elijes: ", elijeUsuario)
    
    if aleatorio == 0:
        elijePc = "piedra"
    elif aleatorio == 1:
        elijePc = "papel"
    elif aleatorio == 2:
        elijePc = "tijera"
    print("PC elijio: ", elijePc)
    print("...")
    