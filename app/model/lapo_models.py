
from google.appengine.ext import ndb


class Jugador(ndb.Model):
    nombre = ndb.StringProperty()
    apodo = ndb.StringProperty()
    imgUrl = ndb.StringProperty()

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "apodo": self.apodo,
            "img": self.imgUrl
        }

    def getPartidas(self):
        partidas = Juego.query().fetch()
        manos = []
        for p in partidas:
            manos += [x for x in p.juegoManos if x.jugador.nombre == self.nombre]
        
        return manos

    def getTotalPuntos(self):
        partidas = self.getPartidas()
        return sum( i.getSum() for i in partidas)

    def getPuntosPorPartida(self):
        puntosTotal = self.getTotalPuntos()
        if puntosTotal > 0:
            return (puntosTotal / len(self.getPartidas()))
        else:
            return 0

    def getMaxPuntaje(self):
        partidas = self.getPartidas()
        if len(partidas) > 0:
            return  max([x.getSum() for x in partidas])
        else:
            return 0

    def getCantidadGanadas(self):
        partidas = self.getPartidas()
        return len([p for p in partidas if p.posicion == 1])    

class Mano(ndb.Model):
    jugador = ndb.StructuredProperty(Jugador)
    manos = ndb.StringProperty()
    posicion = ndb.IntegerProperty()

    def to_dict(self):
        return {
            "jugador": self.jugador.nombre,
            "manos": self.manos
        }
    
    def getSum(self):
        return sum(int(i) for i in self.manos.split(','))

    def getGanadas(self):
        count = 0
        for c in self.manos.split(','):
            if int(c) >= 10:
                count += 1
        return count 

    def getPerdidas(self):
        return len(self.manos.split(',')) - self.getGanadas()

class Juego(ndb.Model):
    fecha = ndb.DateProperty()
    juegoManos = ndb.StructuredProperty(Mano, repeated=True)
    lugar = ndb.StringProperty()
    ganador = ndb.ComputedProperty(lambda self: self.getGanador())

    def to_dict(self):
        return {
            "fecha": self.fecha.strftime("%d/%m/%y"),
            "lugar": self.lugar,
            "manos": [juego.to_dict() for juego in self.juegoManos]
    }

    def getGanador(self):
        ganador = ""
        max = 0
        for jug in self.juegoManos:
            suma = jug.getSum()
            if suma > max:
                max = suma
                ganador = jug.jugador
            
        return ganador.apodo

    def getSortedManos(self):
        return sorted(self.juegoManos, key= lambda mano: mano.getSum(), reverse=True)

