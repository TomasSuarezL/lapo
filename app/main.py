from flask import Flask, render_template, request
from model.lapo_models import Jugador


app = Flask(__name__)

suarez = Jugador(nombre = "Tomas", apodo = "Suarez", imgUrl = "https://images.unsplash.com/photo-1501003878151-d3cb87799705?dpr=1&auto=format&fit=crop&w=750&h=&q=60&cs=tinysrgb&crop=")
godi = Jugador(nombre = "Hueso", apodo = "Godi", imgUrl = "https://images.unsplash.com/photo-1508132128959-17577240b4ce?dpr=1&auto=format&fit=crop&w=334&h=&q=60&cs=tinysrgb&crop=" )
wilk = Jugador(nombre = "Topo", apodo = "Wilki", imgUrl = "https://images.unsplash.com/photo-1506362802973-bd1717de901c?dpr=1&auto=format&fit=crop&w=722&h=&q=60&cs=tinysrgb&crop=")

jugadores = [suarez, godi, wilk]

@app.route('/')
@app.route('/form')
def home():
    return render_template('index.html',jugadores=jugadores)

@app.route('/jugadores')
def getJugadores():
    return render_template('jugadores.html',jugadores=jugadores)
