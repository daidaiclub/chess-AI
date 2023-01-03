from flask import Flask, request
from stockfish import Stockfish

app = Flask(__name__)
stockfish = Stockfish('./stockfish_10_x64')

@app.route('/')
def hello():
  return 'Hello, World!'

@app.route('/ai', methods=['POST'])
def ai():
  stockfish.set_fen_position(request.form['fen'])
  return stockfish.get_best_move()
