from flask import Flask, render_template, request, url_for, jsonify
from datetime import date, datetime
from model.lapo_models import Jugador, Mano, Juego
from model.estadisticas import Estadistica
import logging

# Blueprints
from api.api import api

logging.getLogger().setLevel(logging.DEBUG)
app = Flask(__name__)

app.register_blueprint(api)

suarez = Jugador(nombre = "Tomas", apodo = "Suarez", imgUrl = "/static/images/suarez3.jpg")
godi = Jugador(nombre = "Hueso", apodo = "Godinez", imgUrl = "/static/images/godi1.jpg" )
wilk = Jugador(nombre = "Topo", apodo = "Wilkinson", imgUrl = "/static/images/Topo1.jpg")
vasco = Jugador(nombre = "Igna", apodo = "Vasco", imgUrl = "/static/images/vasco1.jpg")
pares = Jugador(nombre = "Pares", apodo = "Imbecil", imgUrl = "/static/images/pares1.jpg" )
carlitos = Jugador(nombre = "Lucas", apodo = "Carlitos", imgUrl = "/static/images/carlitos1.jpg")
kary = Jugador(nombre = "Karina", apodo = "Kary", imgUrl = "/static/images/kary1.jpg" )
carla = Jugador(nombre = "Carla", apodo = "Pestelina II", imgUrl = "/static/images/carla1.jpg")


jugadores = [suarez, godi, wilk, vasco, pares, carlitos, kary, carla]


@app.route('/')
@app.route('/jugadores/')
def getJugadores():
    jugadoresQ = Jugador.query().fetch()
    return render_template('jugadores.html',jugadores=jugadoresQ)

@app.route('/juegos/')
def getJuegos():
    lapos = Juego.query().fetch()
    return render_template('juegos.html', juegos=lapos)

@app.route('/juegos/<int:juego_id>')
def getJuego(juego_id):
    juego = Juego.get_by_id(juego_id)

    logging.info(juego.juegoManos[0].getSum())
    return render_template('juego.html', juego=juego)

@app.route('/juegos/new', methods=['GET','POST'])
def createJuego():
    if request.method == 'POST':
        juego = request.json['juego']
        lugar = request.json['lugar']
        logging.info(request.json['fecha']['mes'])
        fechaFromRequest = date(int(request.json['fecha']['ano']),int(request.json['fecha']['mes']),int(request.json['fecha']['dia']))
        nuevaLapo = Juego(fecha=fechaFromRequest, juegoManos=[], lugar=lugar)
        logging.info(nuevaLapo)
        for mano in juego:
            jugador = Jugador.query(Jugador.apodo == mano['jugador']).fetch()
            if jugador:
                manos2 = [str(punto) for punto in mano['manos']]
                manoPut = Mano(jugador=jugador[0], manos=','.join(manos2))
                logging.info(manoPut)
                nuevaLapo.juegoManos.append(manoPut)
            else:
                logging.info("No existe jugador")

        nuevaLapo.juegoManos = nuevaLapo.getSortedManos()
        count = 1
        for m in nuevaLapo.juegoManos:
            m.posicion = count
            count+= 1
        nuevaLapo.put()
        logging.info(nuevaLapo)
        return request.form
    else:
        return render_template('nuevoJuego.html')

@app.route('/dashboard')
def getDashboard():
    estadisticas = Estadistica()
    return render_template('dashboard.html',estadisticas=estadisticas)

@app.route('/init')
def iniciar():
    for jugador in jugadores:
        jugador.put()
    return "OK"

