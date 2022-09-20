from flask import *
from random import randint

higherLower = Flask(__name__)

RANDOM_NUMBER = 0


@higherLower.route('/')
def guess():
    global RANDOM_NUMBER
    RANDOM_NUMBER = randint(0, 9)
    return '<center><h1>Guess a number between 0 and 9<h1></br></center>' \
           '<center><img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"></img></center>'


@higherLower.route('/<int:number>')
def check(number):
    response = ''
    if number < RANDOM_NUMBER:
        response = '<center><h1 style="color:red">Too low, try again!<h1></br></center>' \
           '<center><img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"></img></center>'
    elif number > RANDOM_NUMBER:
        response = '<center><h1 style="color:maroon">Too high, try again!<h1></br></center>' \
           '<center><img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"></img></center>'
    else:
        response = '<center><h1 style="color:green">You found me<h1></br></center>' \
           '<center><img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"></img></center>'
    return response


if __name__ == '__main__':
    higherLower.run(debug=True)
