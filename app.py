from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def accueil():
    return render_template('accueil.html')

@app.route('/equipe1')
def equipe1():
    return render_template('equipe1.html')

@app.route('/planning')
def planning():
    return render_template('planning.html')

@app.route('/equipe2')
def equipe2():
    return redirect(/)

@app.route('/contacts')
def contacts():
    return redirect(/)
