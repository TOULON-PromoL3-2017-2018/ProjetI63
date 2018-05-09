import flask
import psycopg2

app = flask.Flask(__name__)
params = "\
  database= sinfo1\
  username= cclain594\
  host= localhost\
  port= 5432\
"

param = {'host': '10.9.186.217'}

try:
    conn = psycopg2.connect(**param)
    print("\n connecté")
except:
    print("\n erreur de connection")
    exit(1)

curr = conn.cursor()

# Me permet d'orienter la recherche des tables dans le schema
curr.execute("SET SEARCH_PATH TO asso")

@app.route('inscription.html', methods=['POST', 'GET'])
def inscription():
    if flask.request.method == 'POST':
        Pseudo = flask.request.form['pseudo']
        Mdp = flask.request.form['mdp']
        Num_étudiant = flask.request.form['Num_Etudiant']
        Mail = flask.request.form['MAIL']
        Rue = flask.request.form['Rue']
        Ville = flask.request.form['Ville']
        Code_postal = flask.request.form['Code_postal']

        query = "INSERT INTO inscrit(pseudo, mdp, Num_Etudiant) \
        VALUES (%s, %s, %d, %s, %s, %s, %s);"

        data = (Pseudo, Mdp, Num_étudiant, Mail, Rue, Ville, Code_postal)
        curr.execute(query, data)
        conn.commit()
        return flask.render_template('inscription_réussi.html', res_nom=nom_etu)

#@app.route('/verif_connection', methods=['POST', 'GET'])
#def connection():


if __name__ == '__main__':

    app.run(debug=True)
