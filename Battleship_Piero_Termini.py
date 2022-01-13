import random
#ESTO ES PARTE VARIABLES.PY
largo_barcos = [1,1,1,1,2,2,2,3,3,4] #estos NO son los numeros oficiales de barcos en el battleship original, 
#deberian ser 2,2,3,3,4,5, 2 corvetas,1 fragata, 1 submarino, un acorazado y un portaviones (me gustaba mucho de pequeno)
tablero_jug = [["  "] * 10 for x in range(10)]
tablero_comp = [["  "] * 10 for x in range(10)]
tablero_jug_disp = [["  "] * 10 for x in range(10)]
tablero_comp_disp = [["  "] * 10 for x in range(10)]
letras_a_numeros = {"A": 0, "B": 1, "C": 2,"D": 3, "E": 4, "F": 5,"G": 6, "H": 7, "I": 8, "J": 9} 


#ESTO ES PARTE DE FUNCIONES.PY
def imp_tablero(tablero):
    print("   A  B  C  D  E  F  G  H  I  J")
    print("---------------------------------")
    num_fila = 1
    for fila in tablero:
        print(str(num_fila) + "|" + "|".join(fila) + "|") 
        #use el join con la variable de fila para que pudisese concatenar en cada fila el simbolo
        num_fila += 1 #esto es para que al imprimir el teclado sea del 1-10 y no 0-9

def pon_barco(tablero):
    #tiene que recorrer la lengitud de los barcos
    for long_barco in largo_barcos:
        #tiene que hacerlo mientras que todos los barcos quepan y no se choquen
        while True:
            if tablero == tablero_comp:
                orientacion, fila, columna = random.choice(["H","V"]), random.randint(0,9), random.randint(0,9) 
                #numpy me dio problemas, decidi hacerlo mas sencillo usando random ya que lo que queria era que crease
                #las posiciones de los barcos al azar, sin embargo, en la version Beta quiero usar Numpy
                if check_barco_cabe(long_barco, fila, columna, orientacion):
                    #hay que chequear que el barco no salga de los limites del tablero
                    if check_barco_choca(tablero, fila, columna, orientacion, long_barco) == False:
                        #hay que chequear que el barco no choque con otro
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
                        #hay que chequear que el barco no salga de los limites del tablero
                        if check_barco_choca(tablero, fila, columna, orientacion, long_barco) == False:
                            #hay que chequear que el barco no choque con otro
                            if orientacion == "H":
                                for i in range(columna, columna + long_barco):
                                    tablero[fila][i] = " X"
                            else:
                                for i in range(fila, fila + long_barco):
                                    tablero[i][columna] = " X"
                            imp_tablero(tablero_jug)
                            break        

#dentro de la funcion barco ya estamos haciendo uso de las dos funciones siguientes, para asegurarnos que los 
#barcos no sobresalen del tablero o chocan entre si

def check_barco_cabe(long_barco, fila, columna, orientacion):
    if orientacion == "H":
        if columna + long_barco > 10:
            return False
        else:
            return True
    else:
        if fila + long_barco > 10:
            return False
        else:
            return True

#con la funcion check_barco_cabe, si el jugador define con su input que el barco ira en vertical u horizontal el
#el programa recorrera las celdas en el sentido indicado y si la suma de la posicion seleccionada + la longitud
#del barco son mayores al tamano del tablero, no permitira posicionar el barco
        
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

#con la funcion check_barco_choca, se hace algo similar a la funcion anterior, solo que en este caso
#el programa recorrera las celdas en el sentido indicado y si el contenido de la celda es X (que hay un barco)
#no permitira al jugador poner otro barco alli

def user_input(pon_barco):
    if pon_barco == True:
        while True:
            try:
                orientacion = input("Selecciona la orientacion, H o V:").upper()
                if orientacion == "H" or orientacion == "V":
                    break
            except TypeError:
                print("Selecciona una orientacion valida, H o V")
        #en el ultimo test run los TypeError, ValueError y KeyError parece que no funcionan correctamente
        #no obstante, no impide la jugabilidad.
        while True:
            try:
                fila = input("Selecciona una fila 1-10:")
                if fila in "12345678910":
                    fila = int(fila) - 1
                    break
            except ValueError:
                print("Selecciona una fila valida, 1-10")
        while True:
            try:
                columna = input("Selecciona una columna A-J:").upper()
                if columna in "ABCDEFGHIJ":
                    columna = letras_a_numeros[columna]
                    break
            except KeyError:
                print("Selecciona una letra valida, A-J")
        return fila, columna, orientacion
    else:
        while True:
            try:
                fila = input("Selecciona una fila 1-10:")
                if fila in "12345678910":
                    fila = int(fila) - 1
                    break
            except ValueError:
                print("Selecciona una fila valida, 1-10")
        while True:
            try:
                columna = input("Selecciona una columna A-J:").upper()
                if columna in "ABCDEFGHIJ":
                    columna = letras_a_numeros[columna]
                    break
            except KeyError:
                print("Selecciona una letra valida, A-J")
        return fila, columna

#esta funcion chequea cada casilla del tablero, si hay una X, la suma al contador.
def cont_disparos_acert(tablero):
    cont = 0
    for fila in tablero:
        for columna in fila:
            if columna == " X":
                cont += 1
    return cont

#si la variable que se la da es tablero_jug_disp, empezara el jugador, de resto empezara la maquina
def turno(tablero):
    if tablero == tablero_jug_disp:
        fila, columna = user_input(tablero_jug_disp)
        if tablero[fila][columna] == "--":
            turno(tablero)
        elif tablero[fila][columna] == " X":
            turno(tablero)
        elif tablero_comp[fila][columna] == " X":
            tablero[fila][columna] = " X"
        else:
            tablero[fila][columna] = "--"
    else:
        fila, columna = random.randint(0,9), random.randint(0,9)
        if tablero[fila][columna] == "--":
            turno(tablero)
        elif tablero[fila][columna] == " X":
            turno(tablero)
        elif tablero_jug[fila][columna] == " X":
            tablero[fila][columna] = " X"
        else:
            tablero[fila][columna] = "--"


#ESTO ES PARTE DEL MAIN.PY
pon_barco(tablero_comp)
imp_tablero(tablero_comp)
imp_tablero(tablero_jug)
pon_barco(tablero_jug)

#start
#input("Bienvenido a BATTLESHIP, quieres hundir la flota enemiga? Si para empezar, No para salir")
#if input() == "Si":
while True:
    #turno del jugador
    while True:
        print("Apunta y di a donde quieres disparar")
        imp_tablero(tablero_jug_disp)
        turno(tablero_jug_disp)
        break
    if cont_disparos_acert(tablero_jug_disp) == 20: #numero de espacios que ocupan los barcos, se debe modificar si
                                                    #se cambian los valores al inicio
        print("Felicidades marinero, has hunido la flota enemiga")
    #turno de la maquina
    while True:
        turno(tablero_comp_disp)
        break
    imp_tablero(tablero_comp_disp)
    if cont_disparos_acert(tablero_comp_disp) == 20:
        print("Lo siento, tus barcos estan todos en el fondo del mar")
        break
#stop
#else:
    #print("Sera en otra ocasion marinero")

#mis puntos a considerar para la version Beta son:

#1-.Reemplazar el tablero hecho con random, por uno hecho con numpy:
#   el problema con numpy me surgio porque queria usar la funcion .choose para elegir V o H y me daba un error que no
#   entendia muy bien

#2-.Separar en Main, Funciones, Variables y Clases el archivo

#3-.Revisar los Errors y corregir ese problema para mejorar la "presentacion"

#4-.agregar una funcion para mejorar la dificultad de la computadora para que pueda disparar multiples veces en un solo
#   turno y ponerlo como nivel de dificultad

#5-.Arreglar el problema del start/stop y anadir Quit

#GRACIAS
