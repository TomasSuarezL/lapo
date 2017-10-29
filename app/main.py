from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/form')
def home():
    return render_template('index.html')

