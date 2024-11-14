import random

def crear_baraja():
    valores = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    baraja = valores * 4
    random.shuffle(baraja)  
    return baraja

def calcularvalorcarta(carta):
    if carta in "JQK":
        return 10
    elif carta == "A":
        return 11
    else:
        return int(carta)

def calcularvalormano(mano):
    valor = sum(calcularvalorcarta(carta) for carta in mano)
    ases = mano.count("A")
    while valor > 21 and ases > 0:
        valor -= 10
        ases -= 1
    return valor

def mostrarmano(mano, es_jugador):
    if es_jugador:
        print("Tu mano es:", *mano)
    else:
        print("La mano de la casa es:", *mano)
    total = str(calcularvalormano(mano))
    print("Total:", total)

def ordenar_mano(mano):
   
    for i in range(len(mano)):
        for j in range(0, len(mano)-i-1):
            if calcularvalorcarta(mano[j]) > calcularvalorcarta(mano[j+1]):
                mano[j], mano[j+1] = mano[j+1], mano[j]

def jugar(baraja):
    mano_jugador = [baraja.pop(), baraja.pop()]
    mano_casa = [baraja.pop()]  

    mostrarmano(mano_jugador, True)
    print("La casa muestra:", mano_casa[0])
    while True:
        opcion = input("¿Quieres pedir otra carta? (s/n): ")
        if opcion.lower() == "s":
            nueva_carta = baraja.pop()
            mano_jugador.append(nueva_carta)
            print("Has recibido:", nueva_carta)
            mostrarmano(mano_jugador, True)
            if calcularvalormano(mano_jugador) > 21:
                print("¡Te has pasado! Pierdes.")
                return
        elif opcion.lower() == "n":
            break
        else:
            print("Por favor, responde con 's' para sí o 'n' para no.")

    while calcularvalormano(mano_casa) < 17:
        nueva_carta = baraja.pop()
        mano_casa.append(nueva_carta)
        print("La casa toma:", nueva_carta)

    mostrarmano(mano_casa, False)

    valor_jugador = calcularvalormano(mano_jugador)
    valor_casa = calcularvalormano(mano_casa)

    if valor_jugador > 21:
        print("¡Te has pasado! Pierdes.")
    elif valor_casa > 21 or valor_jugador > valor_casa:
        print("¡Felicidades! Has ganado.")
    elif valor_jugador == valor_casa:
        print("¡Es un empate!")
    else:
        print("La casa gana.")

   
    ordenar_mano(mano_jugador)
    ordenar_mano(mano_casa)

    print("\nMano final del jugador ordenada:", mano_jugador)
    print("Mano final de la casa ordenada:", mano_casa)

def main():
    print("¡Bienvenido al juego de Blackjack!")
    while True:
        baraja = crear_baraja()
        jugar(baraja)
        continuar = input("¿Quieres jugar otra partida? (s/n): ")
        if continuar.lower() == "n":
            print("¡Gracias por jugar! ¡Hasta luego!")
            break

main()