import random

VALORES_CARTAS = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

class Blackjack:
    def __init__(self):
        self.resetear_partida()

    def resetear_partida(self):
        
        self.baraja = self.crear_baraja()
        self.mano_jugador = []
        self.mano_casa = []
        self.resultado = None

    def crear_baraja(self):
        baraja = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
        random.shuffle(baraja)
        return baraja

    def calcular_puntaje(self, mano):
        puntaje = 0
        ases = 0
        for carta in mano:
            puntaje += VALORES_CARTAS[carta]
            if carta == 'A':
                ases += 1
        while puntaje > 21 and ases:
            puntaje -= 10
            ases -= 1
        return puntaje

    def registrar_resultado(self):
        
        with open("registro_juegos.txt", "a") as archivo:
            archivo.write(f"Resultado: {self.resultado}\n")
            archivo.write(f"Mano del jugador: {self.mano_jugador}\n")
            archivo.write(f"Mano de la casa: {self.mano_casa}\n\n")

    def ordenar_cartas(self, mano):
        mano_ordenada = sorted(mano, key=lambda carta: VALORES_CARTAS[carta])
        return mano_ordenada

    def agregar_carta(self, mano, carta):
        mano.append(carta)

    def eliminar_carta(self, mano, carta):
       
        if carta in mano:
            mano.remove(carta)
            print(f"Carta {carta} eliminada correctamente.")
            print(f"Mano actualizada: {mano}")
        else:
            print(f"La carta {carta} no está en la mano. No se eliminó nada.")
        return mano

    def jugar(self):
        self.resetear_partida()  
        self.mano_jugador.append(self.baraja.pop())
        self.mano_jugador.append(self.baraja.pop())
        self.mano_casa.append(self.baraja.pop())
        self.mano_casa.append(self.baraja.pop())

        print("Tus cartas: ", self.mano_jugador)
        print("Carta visible de la casa: ", self.mano_casa[0])

        while True:
            puntaje_jugador = self.calcular_puntaje(self.mano_jugador)
            if puntaje_jugador > 21:
                print("Te has pasado de 21. Has perdido.")
                self.resultado = "Perdiste"
                self.registrar_resultado()
                return

            accion = input(f"Tu puntaje es {puntaje_jugador}. ¿Quieres pedir otra carta (si) o plantarte (no)? ").lower()
            if accion in ['si', 'sí']:
                carta = self.baraja.pop()
                self.agregar_carta(self.mano_jugador, carta)
                print(f"Has recibido la carta: {carta}")
                print("Tus cartas: ", self.mano_jugador)
            elif accion in ['no', 'n']:
                break
            else:
                print("Opción no válida. Responde con 'si' o 'no'.")

        puntaje_casa = self.calcular_puntaje(self.mano_casa)
        print("Cartas de la casa: ", self.mano_casa)
        while puntaje_casa < 17:
            print("La casa pide carta.")
            carta = self.baraja.pop()
            self.agregar_carta(self.mano_casa, carta)
            puntaje_casa = self.calcular_puntaje(self.mano_casa)
            print("Cartas de la casa: ", self.mano_casa)

        self.mano_jugador = self.ordenar_cartas(self.mano_jugador)
        self.mano_casa = self.ordenar_cartas(self.mano_casa)

        print(f"\nTu mano ordenada: {self.mano_jugador}")
        print(f"Mano de la casa ordenada: {self.mano_casa}")
        print(f"\nTu puntaje: {puntaje_jugador}")
        print(f"Puntaje de la casa: {puntaje_casa}")

        if puntaje_casa > 21:
            print("La casa se ha pasado. ¡Has ganado!")
            self.resultado = "Ganaste"
        elif puntaje_jugador > puntaje_casa:
            print("¡Has ganado!")
            self.resultado = "Ganaste"
        elif puntaje_jugador < puntaje_casa:
            print("La casa gana. Has perdido.")
            self.resultado = "Perdiste"
        else:
            print("Empate.")
            self.resultado = "Empate"

        self.registrar_resultado()

def jugar_otra():
    while True:
        accion = input("¿Quieres jugar otra partida? (si/no): ").lower()
        if accion in ['si', 'sí']:
            return True
        elif accion in ['no', 'n']:
            print("Gracias por jugar!")
            return False
        else:
            print("Respuesta no válida. Responde con 'si' o 'no'.")

def eliminar_cartas(juego):
    while True:
        accion = input("¿Quieres eliminar una carta de tu mano (jugador o casa)? Escribe 'jugador' o 'casa' para seleccionar la mano o 'salir' para terminar: ").lower()
        if accion == 'jugador':
            carta_a_eliminar = input("Escribe el nombre de la carta que deseas eliminar de tu mano: ").upper()
            juego.eliminar_carta(juego.mano_jugador, carta_a_eliminar)
        elif accion == 'casa':
            carta_a_eliminar = input("Escribe el nombre de la carta que deseas eliminar de la mano de la casa: ").upper()
            juego.eliminar_carta(juego.mano_casa, carta_a_eliminar)
        elif accion == 'salir':
            break
        else:
            print("Acción no válida. Escribe 'jugador', 'casa' o 'salir'.")

juego = Blackjack()

while True:
    juego.jugar()
    eliminar_cartas(juego)
    if not jugar_otra():
        break
