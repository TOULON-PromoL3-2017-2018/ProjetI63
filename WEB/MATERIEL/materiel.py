# -*- coding:utf-8 -*-

import time
from flask import *
import psycopg2

app = Flask(__name__)
#param = {'host': '10.9.185.1'}


def connect():
    try:
        print("essaie1")
        conn = psycopg2.connect(dbname='sinfo1')
        print("\n connecté")
        return(conn)
    except psycopg2.Error:
        print("\n erreur de connection")
        exit(1)


@app.route('/', methods=['POST', 'GET'])
def accueil():
    return render_template('acceuil.html')


@app.route('/inscription_reussi/', methods=['GET'])
def inscription_reussi():
    return render_template('incription_reussi.html', nom_user = session['user'][0])

@app.route('/subscription/', methods=['GET', 'POST'])
def subscription():
    if request.method == 'POST':
        pseudo = request.form['pseudo']
        mdp = request.form["mdp"]
        mdp_confirme = request.form["mdp_vérifié"]
        Num_Etudiant = request.form["Num_Etudiant"]
        if (mdp == mdp_confirme):
            query = ("INSERT INTO inscrit (pseudo, mdp, num_Etudiant) VALUES (%s, %s, %s)")
            donnee = (pseudo,mdp,Num_Etudiant)
            curr.execute(query,donnee)
            conn.commit()
            #gestion de session
            session["user"] = donnee[:2]
            return redirect(url_for('inscription_reussi'))

        # flash fournit un moyen de donner un feedback à un utilisateur
        flash("Les mots de passe ne sont pas identiques.")
        # permet de rediriger la personne sur le formulaire d'inscription
        return render_template('inscription.html')
    else:
        return render_template('inscription.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        pseudo = request.form['pseudo']
        mdp = request.form['mdp']
        query = ("SELECT * FROM inscrit WHERE pseudo = %s and mdp = %s")
        donnee = (pseudo , mdp)
        curr.execute(query,donnee)
        donnee_table = curr.fetchall()
        if (len(donnee_table) > 0):
            session['user'] = donnee
            flash("connection réussi")
            return redirect(url_for('acceuil'))
        else:
            flash("Information incorectes")
            return redirect(url_for('inscription'))
    else:
        abort(404)

#@app.route('/catalogue/',met)


if __name__ == '__main__':
    conn = connect()
    curr = conn.cursor()
    # orieente la recherche des table dans le schema
    curr.execute("SET SEARCH_PATH TO asso")
    app.secret_key = "bien chiant"
    app.run(debug=True)
