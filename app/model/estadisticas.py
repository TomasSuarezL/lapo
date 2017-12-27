from lapo_models import Juego, Mano, Jugador


class Estadistica():
    
    def __init__(self):

        juegos = Juego.query().fetch()

        sumPuntos = 0
        cantManos = 0
        maximo = 0

        for p in juegos:
            sumPuntos += sum([x.getSum() for x in p.juegoManos])
            cantManos += len(p.juegoManos)
            maxEnJuego = max([x.getSum() for x in p.juegoManos])
            if maxEnJuego >= maximo:
                maximo = maxEnJuego

        self.cantidadManos = cantManos
        self.puntosTotales = sumPuntos
        self.promedioTotal = sumPuntos / cantManos
        self.cantidadPartidas = len(juegos)
        self.maximoHistorico = maximo
