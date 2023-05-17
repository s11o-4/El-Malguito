import simple_colors
import threading
import time
import Mago
import Jugador


def AtaqueOgro():
    while (True):
        time.sleep(3)
        Jugador1.vida -= 1
        print(simple_colors.red(
            f"\nEl ogro te ha golpeado! Tu vida es de {Jugador1.vida}"))

        print(simple_colors.blue(
            "Para construir una casa, presiona las teclas en orden! 'AWDS' "))

        if (Jugador1.vida <= 0):
            print(simple_colors.red(
                "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"))
            print(simple_colors.red(
                "\n Game Over!, haz muerto... \n Presiona Enter para continuar. "))
            print(simple_colors.red(
                "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"))
            break


# INICIO
def Inicio(Mago, Jugador):
    print()
    print(simple_colors.magenta(
        "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"))
    print(simple_colors.blue("Bienvenido a la villa de las hadas heroe! Oh no! El malvado mago ha secuestrado las hadas, ayudalas construyendo casas para rescatarlas y salvarlas. \nEl mago no se detendra hasta que acabes con todo su poder! Debilitalo rescatando hadas."))
    print(simple_colors.magenta(
        "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"))
    print()

    print(simple_colors.blue(
        f"* El mago tiene {Mago.hada} hadas y {Mago.poder} de poder"))
    print()

    print(simple_colors.blue(
        f"* Cada que construyas 10 casas, ganas 1 de vida y reduces en 1 el poder del mago"))
    print()

    print(simple_colors.blue(
        f"* El mago es astuto, asi que cada que construyas 20 casas el mago destruira 5 casas y robara 5 hadas"))
    print()

    print(simple_colors.blue(
        f"* El jugador ha rescatado {Jugador.hada} hadas, su vida es de {Jugador.vida} y tiene {Jugador.poder} de poder"))
    print()

    print(simple_colors.blue(
        f"* El Ogro es invensible. Acaba con el Mago salvando a las hadas!"))
    print()

    print(simple_colors.blue(
        f"* Vamos, construye lo más rapido que puedas!"))
    print()

    print(simple_colors.magenta("||||||Preciona Enter para Iniciar||||||"))
    input()

    return

# ACCIÓN
def Accion(Mago, Jugador):
    flag = 0

    if (Jugador1.vida <= 0):
        flag = 2
        return flag 

    # print()
    boton = input(simple_colors.blue(
        "Para construir una casa, presiona las teclas en orden! 'AWDS' "))
    # print()

    #Si la vida del jugador ya termino, entonces sale del programa
    if (Jugador1.vida <= 0):
        flag = 2
        return flag 
    
    else:
        if boton == 'AWDS' or boton == 'awds':
            Jugador.casa += 1
            print(
                f"Tienes: {Jugador.casa} casas por lo que has rescatado 1 hada más! Hadas rescatadas: {Jugador.casa}")
        else:
            print("Tienes que presionar 'AWDS' en orden! ")

    # cada que construya 10 casas, 10 hadas seran rescatadas y el jugador ganara 1 de poder y 1 de vida, tambien por cada 10 hadas el Mago perdera 1 de poder
    while ((Jugador.casa % 10) == 0):
        Jugador.vida += 1
        Jugador.poder += 1
        Magito.poder -= 1
        Magito.hada -= 10
        print()
        print(simple_colors.magenta(
            f"Felicidades has rescatado 10 hadas! has recuperado vida y poder! Tu vida aumento 1: {Jugador.vida} y tu poder es {Jugador.poder}.\n\nEl mago se ha debilitado; tiene {Magito.poder} de poder y {Magito.hada} hadas"))
        # Si llega a selo la bandera se vuelve verdadera y se acaba el juego
        if Magito.hada == 0:
            flag = True
            # print("Felicidades el mago ha sido derrotado!! Gracias heroe!")

        break

    # cada 20 casas el mago destruira 5 casas y robara 5 hadas... No lo hace, cada que llega a 20 roba hadas...
    while (Jugador.casa % 20) == 0:
        if flag == True:
            break
        else:
            Magito.hada += 5
            Jugador.casa -= 5
            Magito.poder = int(Magito.hada/10)
            print(simple_colors.magenta(
                f" \n Oh no! el mago ha destruido 5 casas y ha robado 5 hadas! El mago tiene {Magito.hada} hadas y {Magito.poder} poder"))
    return flag

# FIN


def Fin(Mago, Jugador):
    c = True
    while c == True:
        if (Accion(Magito, Jugador1) == 1):
            print(simple_colors.blue(
                "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"))
            print(simple_colors.magenta(
                "\n Felicidades el mago ha sido derrotado!! Gracias heroe! ᕕ( ᐛ )ᕗ \n "))
            print(simple_colors.blue(
                "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"))
            break
        elif (Accion(Magito, Jugador1) == 2):
            break
    return


# Declaracion de objetos
Magito = Mago.Mago()
Jugador1 = Jugador.Jugador()


Inicio(Magito, Jugador1)

#Todo esto inicia despues de llamar a la funcion inicio
# Creo un objeto de la clase threading la cual me permite crear subprocesos
# le paso como argumento la funcion que quiero que ejecute en segundi plano
hilo = threading.Thread(target=AtaqueOgro)
# configura el hilo para que se detenga automaticamente cuando el programa principal
# acabe
hilo.daemon = True
# comienza el hilo
hilo.start()


Accion(Magito, Jugador1)
Fin(Magito, Jugador1)
