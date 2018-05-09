import flask
import psycopg2
from datetime import datetime


app = flask.Flask(__name__)
params = {
  'host': 'localhost'
}
try:
    conn = psycopg2.connect(**params)
    print("\n connecté")
except:
    print("\n erreur de connection")


cur = conn.cursor()

@app.route('/validation_inscription/', methods=['POST', 'GET'])
def inscription():
    if flask.request.method == 'POST':
        pseudo = flask.request.form['pseudo']
        mdp = flask.request.form['mdp']
        num_étudiant = flask.request.form['Num_Etudiant']

        query = "INSERT INTO inscrit(pseudo, mdp, Num_Etudiant) VALUES (%s, %s, %d);"

@app.route('/verif_connection', methods=['POST', 'GET'])
def connection():
