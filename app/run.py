
from flask import Flask, request
from game import game

app = Flask(__name__)

@app.post("/")
def challengeSetup():
    req = request.get_json()
    words = req['words']
    strikes = req['strikes']
    is_one_away = req['isOneAway']
    correct_groups = req['correctGroups']
    previous_guesses = req['previousGuesses']
    error = req['error']

    guess, endTurn = game.model(words, strikes, is_one_away, correct_groups, previous_guesses, error)
    
    return guess, endTurn