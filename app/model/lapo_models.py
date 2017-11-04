
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

