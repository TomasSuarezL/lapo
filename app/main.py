from flask import Flask, render_template, request
from model.lapo_models import Jugador


app = Flask(__name__)

suarez = Jugador(nombre = "Tomas", apodo = "Suarez", imgUrl = "https://images.unsplash.com/photo-1501003878151-d3cb87799705?dpr=1&auto=format&fit=crop&w=750&h=&q=60&cs=tinysrgb&crop=")
godi = Jugador(nombre = "Hueso", apodo = "Godi", imgUrl = "https://images.unsplash.com/photo-1508132128959-17577240b4ce?dpr=1&auto=format&fit=crop&w=334&h=&q=60&cs=tinysrgb&crop=" )
wilk = Jugador(nombre = "Topo", apodo = "Wilki", imgUrl = "https://images.unsplash.com/photo-1506362802973-bd1717de901c?dpr=1&auto=format&fit=crop&w=722&h=&q=60&cs=tinysrgb&crop=")
vasco = Jugador(nombre = "Igna", apodo = "Vasco", imgUrl = "https://images.unsplash.com/photo-1501003878151-d3cb87799705?dpr=1&auto=format&fit=crop&w=750&h=&q=60&cs=tinysrgb&crop=")
pares = Jugador(nombre = "Pares", apodo = "Imbecil", imgUrl = "https://images.unsplash.com/photo-1508132128959-17577240b4ce?dpr=1&auto=format&fit=crop&w=334&h=&q=60&cs=tinysrgb&crop=" )
carlitos = Jugador(nombre = "Lucas", apodo = "Carlitos", imgUrl = "https://images.unsplash.com/photo-1506362802973-bd1717de901c?dpr=1&auto=format&fit=crop&w=722&h=&q=60&cs=tinysrgb&crop=")


jugadores = [suarez, godi, wilk, vasco, pares, carlitos]

@app.route('/')
@app.route('/jugadores/')
def getJugadores():
    return render_template('jugadores.html',jugadores=jugadores)

@app.route('/juegos/')
def getJuegos():
    return render_template('juegos.html')


@app.route('/juegos/new', methods=['GET','POST'])
def createJuego():
    if request.method == 'POST':
        pass
    else:
        return render_template('nuevoJuego.html')

@app.route('/dashboard')
def getDashboard():
    return render_template('dashboard.html',jugadores=jugadores)