# -*- coding:utf-8 -*-

from __future__ import print_function
import time
from flask import *
import psycopg2
import smtplib


app = Flask(__name__)
# param = {'host': '10.9.185.1'}


# ____ FONCTION PYTHON SIMPLE ____
def connect():
    try:
        print("essaie1")
        return(psycopg2.connect(dbname='sinfo1'))
    except psycopg2.Error:
        print("\n erreur de connection")
        exit(1)


def update_table_stock():
    # affichage du tuple
    # print("\n\n\n\n", session['pigeon'], "\n\n\n\n")
    query = ("SELECT intitule_materiel, quantite FROM materiel_stock")
    curr.execute(query)
    donnee = curr.fetchall()
    # print("\n\n\n\n\n",donnee,"\n\n\n\n\n")
    for i, article in enumerate(session['pigeon']):
        # print("\n\n\n\n", session['pigeon'][i], "\n\n\n\n")
        j = 0
        while j < len(donnee):
            if session['pigeon'][i][0] == donnee[j][0]:
                intitule_materiel = donnee[j][0]
                # print("\n\n\n\n", intitule_materiel, "\n\n\n\n\n\n")
                new_quantite_stock = int(donnee[j][1]) - int(session['pigeon'][i][1])
                new_quantite_stock = str(new_quantite_stock)
                # print(new_quantite_stock)
                query = " UPDATE materiel_stock set quantite = %s WHERE intitule_materiel = %s"
                curr.execute(query, (new_quantite_stock, donnee[j][0]))
                conn.commit()
                print("fin du commit")
            j += 1


def incrementation_pigeon(nom_article, quantite, prix):
    # print("\n\n\n\n", type(nom_article), "\n\n\n\n")
    curr.execute("SELECT quantite FROM materiel_stock WHERE intitule_materiel = %s", (nom_article,))
    conn.commit()
    quantite_en_stock = curr.fetchall()
    # print("\n\n\n\n", quantite_en_stock, "\n\n\n\n")
    index = -1
    # cherche si l'article est dejà present dans le panier
    for i, article in enumerate(session['pigeon']):
        if nom_article in article:
            index = i
    # cas ou l'article est dans le panier
    if index != -1:
        var = (session['pigeon'][index][1] + quantite)
        if (var > quantite_en_stock[0][0]):
            return(var)
        session['pigeon'][index][1] = var
        return(session['pigeon'][index][1])
    # cas 1ère commande de cet article dans le panier actuelle
    # necessite que la quantite soit inferieur au stock
    # problème : 30 est la quantite de depart mais si j'ai 40 objet en stock la
    # fonction utilisant une constante et non une variable sera a modifier
    elif (quantite <= quantite_en_stock[0][0]):
        session['pigeon'] += [[nom_article, quantite, prix]]
        return(session['pigeon'][0][1])
    # retourne faux car on demande + d'article que le stock
    return(quantite)


def peut_acheter(donnee, intitule_materiel, quantite_total_commande):
    for i in enumerate(donnee):
        if i[1][0] == intitule_materiel:
            return((int(i[1][1]) >= quantite_total_commande))


# mail de l'entreprise : projetI63 mdp : projet_I63
# mail du client projetI63client mdp : projet_I63
def send_mail(email, msg):
    serveur = smtplib.SMTP('smtp.gmail.com', 587)
    serveur.starttls()
    serveur.login("projetI63client", "projet_I63")
    serveur.sendmail("projetI63client", "projetI63@gmail.com", msg)
    serveur.quit()


def reponse_auto(email):
    serveur = smtplib.SMTP('smtp.gmail.com', 587)
    serveur.starttls()
    serveur.login("projetI63", "projet_I63")
    msg= " Message recu"
    serveur.sendmail("projetI63", "projetI63client@gmail.com", msg)

# ____ FONCTION APP.ROUTE____
@app.route('/mail/', methods=['POST'])
def mail():
    email = request.form['mail']
    # print("\n\n\n", email, "\n\n\n")
    msg = request.form['message']
    # print("\n\n\n", msg, "\n\n\n")
    send_mail(email, msg)
    reponse_auto(email)
    return redirect(url_for('accueil'))

@app.route('/', methods=['POST', 'GET'])
def accueil():
    return render_template('acceuil.html', est_connecte=('user' in session))


@app.route('/inscription_reussi/', methods=['GET'])
def inscription_reussi():
    return render_template('incription_reussi.html', nom_user=session['user'][0])

@app.route('/logout/', methods=['GET'])
def logout():
    session.pop('user')
    session.pop('pigeon')
    return redirect(url_for('accueil'))

@app.route('/subscription/', methods=['GET', 'POST'])
def subscription():
    if request.method == 'POST':
        pseudo = request.form['pseudo']
        mdp = request.form["mdp"]
        mdp_confirme = request.form["mdp_verifie"]
        Num_Etudiant = request.form["Num_Etudiant"]
        if (mdp == mdp_confirme):
            query = ("INSERT INTO inscrit (pseudo, mdp, num_Etudiant) \
            VALUES (%s, %s, %s)")
            donnee = (pseudo, mdp, Num_Etudiant)
            curr.execute(query, donnee)
            conn.commit()
            #gestion de session
            session["user"] = donnee[:2]
            session["pigeon"] = []
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
        donnee = (pseudo, mdp)
        curr.execute(query, donnee)
        donnee_table = curr.fetchall()
        if (len(donnee_table) > 0):
            session["pigeon"] = []
            session['user'] = donnee
            message_flash = "connection reussi "+donnee[0]
            flash(message_flash)
            return redirect(url_for('accueil'))

        flash("Information incorectes")
        return redirect(url_for('subscription'))
    else:
        abort(404)


def verif(cb):
    liste_de_chiffre = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    i = 0
    while (i < len(cb)):
        if (cb[i] not in liste_de_chiffre):
            return(False)
        i += 1
    return(True)


@app.route('/verif_carte/', methods=['GET', 'POST'])
def verif_carte():
    if request.method == 'POST':
        cb1 = request.form['num_cb1']
        if (not(verif(cb1))):
            flash("numero de carte bleu invalide")
            return render_template('form_cb.html')
        cb2 = request.form['num_cb2']
        if (not(verif(cb2))):
            flash("numero de carte bleu invalide")
            return render_template('form_cb.html')
        cb3 = request.form['num_cb3']
        if (not(verif(cb3))):
            flash("numero de carte bleu invalide")
            return render_template('form_cb.html')
        cb4 = request.form['num_cb4']
        if (not(verif(cb4))):
            flash("numero de carte bleu invalide")
            return render_template('form_cb.html')
        crypt = request.form['cryptogramme_visuel']
        if (not(verif(crypt))):
            flash("cryptogramme visuel invalide")
            return render_template('form_cb.html')
    flash("paiement effectué")
    update_table_stock()
    session["pigeon"] = []
    return redirect(url_for('accueil'))


@app.route('/catalogue/', methods=['GET', 'POST'])
def catalogue():
    query = ("SELECT intitule_materiel, quantite, prix_unite_hf \
    FROM materiel_stock, type_materiel \
    WHERE materiel_stock.Ref_Type_Materiel = type_materiel.Ref_Type_Materiel")
    curr.execute(query)
    donnee = curr.fetchall()
    if request.method == 'POST':
        quantite_acheter = int(request.form['quantite'])
        intitule_materiel = request.form['intitule_materiel']
        prix_u_hf = int(request.form['prix_u_hf'])
        quantite_total_commande = incrementation_pigeon(intitule_materiel,
                                                        quantite_acheter,
                                                        prix_u_hf)
        if (peut_acheter(donnee, intitule_materiel, quantite_total_commande)):
            flash("ajout au panier")
        else:
            flash("pas assez en stock")
            return render_template("catalogue.html", pigeon=donnee,
                                   est_connecte=('user' in session))
    return render_template("catalogue.html", pigeon=donnee,
                           est_connecte=('user' in session))


@app.route('/panier/', methods=['GET'])
def panier():
    # print("\n\n\n", session["pigeon"], "\n\n\n")
    return render_template("panier.html", articles=session["pigeon"])


@app.route('/payer/', methods=['GET'])
def payer():
    return render_template("form_cb.html")


if __name__ == '__main__':
    conn = connect()
    curr = conn.cursor()
    # oriente la recherche des table dans le schema
    curr.execute("SET SEARCH_PATH TO asso")
    app.secret_key = "bien chiant"
    app.run(debug=True)
