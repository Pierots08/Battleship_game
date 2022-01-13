import random

largo_barcos = [1,2,3,2,2]
tablero_jug = [["  "] * 5 for x in range(5)]
tablero_comp = [["  "] * 5 for x in range(5)]
tablero_jug_disp = [["  "] * 5 for x in range(5)]
tablero_comp_disp = [["  "] * 5 for x in range(5)]
letras_a_numeros = {"A": 0, "B": 1, "C": 2,"D": 3, "E": 4} 

#Funciones
#---------------------------------------------------------------------------------------------------------------#


def imp_tablero(tablero):
    print("   A  B  C  D  E")
    print("----------------")
    num_fila = 1
    for fila in tablero:
        print(str(num_fila) + "|" + "|".join(fila) + "|")
        num_fila += 1

def pon_barco(tablero):
    for long_barco in largo_barcos:
        while True:
            if tablero == tablero_comp:
                orientacion, fila, columna = random.choice(["H","V"]), random.randint(0,4), random.randint(0,4)
                if check_barco_cabe(long_barco, fila, columna, orientacion):
                    if check_barco_choca(tablero, fila, columna, orientacion, long_barco) == False:
                        if orientacion == "H":
                            for i in range(columna, columna + long_barco):
                                tablero[fila][i] = " X"
                        else:
                            for i in range(fila, fila + long_barco):
                                tablero[i][columna] = " X"
                        break
            else:
                pon_barco = True
                print("pon el barco con la longitud de: " + str(long_barco))
                fila, columna, orientacion = user_input(pon_barco)
                if check_barco_cabe(long_barco, fila, columna, orientacion):
                        if check_barco_choca(tablero, fila, columna, orientacion, long_barco) == False:
                            if orientacion == "H":
                                for i in range(columna, columna + long_barco):
                                    tablero[fila][i] = " X"
                            else:
                                for i in range(fila, fila + long_barco):
                                    tablero[i][columna] = " X"
                            imp_tablero(tablero_jug)
                            break        


def check_barco_cabe(long_barco, fila, columna, orientacion):
    if orientacion == "H":
        if columna + long_barco > 5:
            return False
        else:
            return True
    else:
        if fila + long_barco > 5:
            return False
        else:
            return True
        
def check_barco_choca(tablero, fila, columna, orientacion, long_barco):
    if orientacion == "H":
        for i in range(columna, columna + long_barco):
            if tablero[fila][i] == " X":
                return True
    else:
        for i in range(fila, fila + long_barco):
            if tablero[i][columna] == " X":
                return True
    return False

def user_input(pon_barco):
    if pon_barco == True:
        while True:
            try:
                orientacion = input("Selecciona la orientacion, H o V:").upper()
                if orientacion == "H" or orientacion == "V":
                    break
            except TypeError:
                print("Selecciona una orientacion valida, H o V")
        while True:
            try:
                fila = input("Selecciona una fila 1-5:")
                if fila in "1" or "2" or "3" or "4" or "5":
                    fila = int(fila) - 1
                    break
            except ValueError:
                print("Selecciona una fila valida, 1-5")
        while True:
            try:
                columna = input("Selecciona una columna A-E:").upper()
                if columna in "ABCDE":
                    columna = letras_a_numeros[columna]
                    break
            except KeyError:
                print("Selecciona una letra valida, A-E")
        return fila, columna, orientacion
    else:
        while True:
            try:
                fila = input("Selecciona una fila 1-5:")
                if fila in "1" or "2" or "3" or "4" or "5":
                    fila = int(fila) - 1
                    break
            except ValueError:
                print("Selecciona una fila valida, 1-5")
        while True:
            try:
                columna = input("Selecciona una columna A-E:").upper()
                if columna in "ABCDE":
                    columna = letras_a_numeros[columna]
                    break
            except KeyError:
                print("Selecciona una letra valida, A-E")
        return fila, columna


def cont_disparos_acert(tablero):
    cont = 0
    for fila in tablero:
        for columna in fila:
            if columna == " X":
                cont += 1
    return cont

def turno(tablero):
    if tablero == tablero_jug_disp:
        fila, columna = user_input(tablero_jug_disp)
        if tablero[fila][columna] == "--":
            turno(tablero)
        elif tablero[fila][columna] == " X":
            turno(tablero_jug_disp)
        elif tablero_comp[fila][columna] == " X":
            tablero[fila][columna] = " X"
        else:
            tablero[fila][columna] = "--"
    else:
        fila, columna = random.randint(0,4), random.randint(0,4)
        if tablero[fila][columna] == "--":
            turno(tablero)
        elif tablero[fila][columna] == " X":
            turno(tablero_comp_disp)
        elif tablero_jug[fila][columna] == " X":
            tablero[fila][columna] = " X"
        else:
            tablero[fila][columna] = "--"

#Main
#---------------------------------------------------------------------------------------------------------------#

pon_barco(tablero_comp)
imp_tablero(tablero_comp)
imp_tablero(tablero_jug)
pon_barco(tablero_jug)

while True:
    #turno del jugador
    while True:
        print("Apunta y di a donde quieres disparar")
        imp_tablero(tablero_jug_disp)
        turno(tablero_jug_disp)
        break
    if cont_disparos_acert(tablero_jug_disp) == 10: #numero de espacios que ocupan los barcos
        print("Felicidades marinero, has hunido la flota enemiga")
    #turno de la maquina
    while True:
        turno(tablero_comp_disp)
        break
    imp_tablero(tablero_comp_disp)
    if cont_disparos_acert(tablero_comp_disp) == 10:
        print("Lo siento, tus barcos estan todos en el fondo del mar")
        break

    #Gracias

