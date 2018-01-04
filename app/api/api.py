
# import logging
from model.lapo_models import  Jugador, Juego
from flask import Blueprint, jsonify



api = Blueprint('api', 'api', url_prefix='/api')


@api.route('/graficos', methods=['GET'])
def getData():
    jugadores = Jugador.query().fetch()
    jsonReturn = {}
    ganadores = {}
    lugares = {}
    anos = {}

    for j in jugadores:
        ganadores[j.apodo] = len(Juego.query(Juego.ganador == j.apodo).fetch())

    juegos = Juego.query().fetch()

    for j in juegos:
        if j.lugar in lugares:
            lugares[j.lugar] += 1
        else:
            lugares[j.lugar] = 1

        if j.fecha.year in anos:
            anos[j.fecha.year] += 1
        else:
            anos[j.fecha.year] = 1

    jsonReturn['ganadores'] = ganadores
    jsonReturn['lugares'] = lugares
    jsonReturn['anos'] = anos

    return jsonify(jsonReturn)
