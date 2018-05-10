# -*- coding:utf-8 -*-

import time
from flask import *
import psycopg2

app = Flask(__name__)
param = {'host': '127.0.0.1'}

try:
    conn = psycopg2.connect(**param)
    print("\n connecté")
except psycopg2.Error:
    print("\n erreur de connection")
    exit(1)

curr = conn.cursor()
# orieente la recherche des table dans le schema
curr.execute("SET SEARCH_PATH TO asso")


@app.route('/', methods=['POST', 'GET'])
def accueil():
    return render_template('accueil.html')

@app.route('/subscription/', methods=['GET', 'POST'])
def subscription():
    if request.method == 'POST':
        pseudo = request.form['pseudo']
        mdp = request.form["mdp"]
        mdp_confirme = request.form["mdp_vérifié"]
        if (mdp == mdp_confirme):
            query = "INSERT INTO inscrit(pseudo, mdp, Num_Etudiant) VALUES (%s, %s, %d);"
            return redirect(url_for('inscription_reussi'))
            curr.execute(query)
            conn.commit()

        # flash fournit un moyen de donner un feedback à un utilisateur
        flash("Les mots de passe ne sont pas identiques.")
        # permet de rediriger la personne sur le formulaire d'inscription
        return redirect(url_for('inscription'))
    else:
        abort(404)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        pseudo = request.form['pseudo']
        mdp = request.form['mdp']
        curr.execute("SELECT pseudo, mdp FROM inscrit")
        donnee = curr.fetchall()
        if (len(donnee) == 2):
            if ((donne[0] == pseudo) and (donnee[1] == mdp)):
                flash("connection réussi")
        flash("Information incorectes")
        return redirect(url_for('inscription'))

if __name__ == '__main__':
    app.run(debug=True)
