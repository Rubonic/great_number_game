from operator import truediv
from flask import Flask, render_template, request, redirect, session
import random, math
app = Flask(__name__)
app.secret_key = 'no more rhymes I mean it!'

@app.route('/')
def index():
    if 'magicNum' not in session:
        session['magicNum'] = random.randint(1,100)
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def processGuess():
    session['guess'] = int(request.form['guess'])
    print('guess saved!')

    return redirect ('/')

@app.route('/destroy_session')
def destroySession():
    session.clear()

    return redirect ('/')



if __name__ == "__main__":
    app.run(debug=True)