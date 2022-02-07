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
    #  3
    if elijePc == "piedra" and elijeUsuario == "papel":
        print("Ganaste, papel envulve piedra")
    elif elijePc == "papel" and elijeUsuario == "tijera":
        print("Ganaste, Tijera corta papel")
    elif elijePc == "tijera" and elijeUsuario == "piedra":
        print("Ganaste, Piedra pisa tijera")
    if elijePc == "papel" and elijeUsuario == "piedra":
        print("perdiste, papel envulve piedra")
    elif elijePc == "tijera" and elijeUsuario == "papel":
        print("perdiste, Tijera corta papel")
    elif elijePc == "piedra" and elijeUsuario == "tijera":
        print("perdiste, Piedra pisa tijera")
    elif elijePc == elijeUsuario:
        print("empate")
    if idioma == 2:
        print("You put the game in english")
        aleatorio = random.randrange(0, 3)
        elijePc = ""
        print("1)Rock")
        print("2)Paper")
        print("3)Scissors")
        opcion = int(input("Make a choice: "))
        # 4
    if opcion == 1:
        elijeUsuario = "Rock"
    elif opcion == 2:
        elijeUsuario = "Paper"
    elif opcion == 3:
        elijeUsuario = "Scissors"
    print("Your choice: ", elijeUsuario)
     # 5
    if aleatorio == 0:
        elijePc = "Rock"
    elif aleatorio == 1:
        elijePc = "Paper"
    elif aleatorio == 2:
        elijePc = "Scissors"
    print("Enemy choice: ", elijePc)
    print("...")