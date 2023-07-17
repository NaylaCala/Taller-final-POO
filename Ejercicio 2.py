import random

class Carta:
    def __init__(self, palo, valor):
        self.palo = palo
        self.valor = valor

    def __str__(self):
        return f"{self.valor} de {self.palo}"

class Mazo:
    def __init__(self):
        self.cartas = []
        self.crear_mazo()

    def crear_mazo(self):
        palos = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
        valores = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jota', 'Reina', 'Rey']

        for palo in palos:
            for valor in valores:
                self.cartas.append(Carta(palo, valor))

    def barajar(self):
        random.shuffle(self.cartas)

    def repartir_carta(self):
        return self.cartas.pop()

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.manos = [[]]
        self.puntajes = [0]

    def recibir_carta(self, mano_idx, carta):
        self.manos[mano_idx].append(carta)

    def obtener_puntaje(self, mano_idx):
        puntaje = 0
        aces = 0

        for carta in self.manos[mano_idx]:
            if carta.valor == 'As':
                puntaje += 11
                aces += 1
            elif carta.valor in ['Rey', 'Reina', 'Jota']:
                puntaje += 10
            else:
                puntaje += int(carta.valor)

        while puntaje > 21 and aces > 0:
            puntaje -= 10
            aces -= 1

        return puntaje

    def dividir_mano(self, mano_idx):
        carta = self.manos[mano_idx].pop()
        nueva_mano = [carta]
        self.manos.append(nueva_mano)
        self.puntajes.append(self.obtener_puntaje(mano_idx))
        self.puntajes[mano_idx] = self.obtener_puntaje(mano_idx)

class JuegoBlackjack:
    def __init__(self, nombre_jugador):
        self.jugador = Jugador(nombre_jugador)
        self.dealer = Jugador("Crupier")
        self.mazo = Mazo()

    def repartir_cartas_iniciales(self):
        self.mazo.barajar()

        for _ in range(2):
            self.jugador.recibir_carta(0, self.mazo.repartir_carta())
            self.dealer.recibir_carta(0, self.mazo.repartir_carta())

    def turno_jugador(self, mano_idx):
        while True:
            print(f"\nMano {mano_idx + 1} del Jugador:")
            for carta in self.jugador.manos[mano_idx]:
                print(carta)

            print(f"Puntaje de la Mano {mano_idx + 1} del Jugador:", self.jugador.obtener_puntaje(mano_idx))

            eleccion = input("\n¿Deseas pedir una carta más(p), plantarte(l) o dividir(d)?: ")
            if eleccion.lower() == 'p':
                self.jugador.recibir_carta(mano_idx, self.mazo.repartir_carta())

                if self.jugador.obtener_puntaje(mano_idx) > 21:
                    print(f"\nPuntaje de la Mano {mano_idx + 1} del Jugador:", self.jugador.obtener_puntaje(mano_idx))
                    print(f"¡El Jugador se pasa de 21 en la Mano {mano_idx + 1}! Gana el Crupier.")
                    return
            elif eleccion.lower() == 'l':
                break
            elif eleccion.lower() == 'd':
                if len(self.jugador.manos[mano_idx]) == 2 and self.jugador.manos[mano_idx][0].valor == self.jugador.manos[mano_idx][1].valor:
                    self.jugador.dividir_mano(mano_idx)
                else:
                    print("¡No puedes dividir en esta mano!")

    def turno_dealer(self):
        while self.dealer.obtener_puntaje(0) < 17:
            self.dealer.recibir_carta(0, self.mazo.repartir_carta())

        print("\nMano del Crupier:")
        for carta in self.dealer.manos[0]:
            print(carta)
        print("Puntaje de la Mano del Crupier:", self.dealer.obtener_puntaje(0))

        if self.dealer.obtener_puntaje(0) > 21:
            print("¡El Crupier se pasa de 21! Gana el Jugador.")
        else:
            for i, puntaje in enumerate(self.jugador.puntajes):
                if puntaje > self.dealer.obtener_puntaje(0):
                    print(f"¡Gana el Jugador en la Mano {i + 1}!")
                elif puntaje < self.dealer.obtener_puntaje(0):
                    print(f"¡Gana el Crupier en la Mano {i + 1}!")
                else:
                    print(f"¡Empate en la Mano {i + 1}!")

    def jugar(self):
        print("¡Bienvenido a Blackjack!")

        self.repartir_cartas_iniciales()
        for i in range(len(self.jugador.manos)):
            self.turno_jugador(i)
        self.turno_dealer()

        print("\n¡Gracias por jugar!")

# Ejemplo de uso
juego = JuegoBlackjack("Jugador 1")
juego.jugar()
