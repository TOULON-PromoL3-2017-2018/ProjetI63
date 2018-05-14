# -*- coding:utf-8 -*-

from __future__ import print_function
import time
import flask
import psycopg2
import smtplib


app = flask.Flask(__name__)
param = {'host': '10.9.185.1'}

#dbname='sinfo1'

# ____ FONCTION PYTHON SIMPLE ____
def connect():
    try:
        # print("essaie1")
        return(psycopg2.connect(**param))
    except psycopg2.Error:
        print("\n erreur de connection")
        exit(1)


def update_table_caution():
    # print("\n\n\n\n", flask.session['user'], "\n\n\n\n")
    prix_tot = 0
    for i, article in enumerate(flask.session['pigeon']):
        j = 0
        while j < flask.session['pigeon'][i][1]:
            prix_tot = prix_tot + flask.session['pigeon'][i][2]
            j += 1
    num_etude = flask.session['user'][0][2]
    donnee = (prix_tot, num_etude)
    query = ("INSERT INTO Caution(Prix_Caution, Num_Etudiant) VALUES (%s,%s)")
    curr.execute(query, donnee)
    conn.commit()


def update_table_stock():
    # affichage du tuple
    # print("\n\n\n\n", flask.session['pigeon'], "\n\n\n\n")
    query = ("SELECT intitule_materiel, quantite FROM materiel_stock")
    curr.execute(query)
    donnee = curr.fetchall()
    # print("\n\n\n\n\n",donnee,"\n\n\n\n\n")
    for i, article in enumerate(flask.session['pigeon']):
        # print("\n\n\n\n", flask.session['pigeon'][i], "\n\n\n\n")
        j = 0
        while j < len(donnee):
            if flask.session['pigeon'][i][0] == donnee[j][0]:
                intitule_materiel = donnee[j][0]
                # print("\n\n\n\n", intitule_materiel, "\n\n\n\n\n\n")
                new_quantite_stock = int(donnee[j][1]) - int(flask.session['pigeon'][i][1])
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
    for i, article in enumerate(flask.session['pigeon']):
        if nom_article in article:
            index = i
    # cas ou l'article est dans le panier
    if index != -1:
        var = (flask.session['pigeon'][index][1] + quantite)
        if (var > quantite_en_stock[0][0]):
            return(var)
        flask.session['pigeon'][index][1] = var
        return(flask.session['pigeon'][index][1])
    # cas 1ère commande de cet article dans le panier actuelle
    # necessite que la quantite soit inferieur au stock
    # problème : 30 est la quantite de depart mais si j'ai 40 objet en stock la
    # fonction utilisant une constante et non une variable sera a modifier
    elif (quantite <= quantite_en_stock[0][0]):
        flask.session['pigeon'] += [[nom_article, quantite, prix]]
        return(flask.session['pigeon'][0][1])
    # retourne faux car on demande + d'article que le stock
    return(quantite)


def peut_acheter(donnee, intitule_materiel, quantite_total_commande):
    for i in enumerate(donnee):
        if i[1][0] == intitule_materiel:
            return((int(i[1][1]) >= quantite_total_commande))


# mail de l'entreprise : projetI63 mdp : projet_I63
# mail du client projetI63client mdp : projet_I63
def send_mail(email, msg, mdp):
    serveur = smtplib.SMTP('smtp.gmail.com', 587)
    serveur.starttls()
    serveur.login(email, mdp)
    serveur.sendmail(email, "projetI63@gmail.com", msg)
    serveur.quit()


def reponse_auto(email):
    serveur = smtplib.SMTP('smtp.gmail.com', 587)
    serveur.starttls()
    serveur.login("projetI63", "projet_I63")
    msg= " Message recu"
    mail = email+'@gmail.com'
    serveur.sendmail("projetI63", mail, msg)


# ____ FONCTION APP.ROUTE____
@app.route('/mail/', methods=['POST'])
def mail():
    email = flask.request.form['mail']
    print("\n\n\n", email, "\n\n\n")
    msg = flask.request.form['message']
    # print("\n\n\n", msg, "\n\n\n")
    mdp_mail = flask.request.form['mdp_mail']
    send_mail(email, msg, mdp_mail)
    reponse_auto(email)
    return flask.redirect(flask.url_for('accueil_mat'))

@app.route('/accueil_mat/', methods=['POST', 'GET'])
def accueil_mat():
    return flask.render_template('acceuil.html', est_connecte=('user' in flask.session))


@app.route('/inscription_reussi/', methods=['GET'])
def inscription_reussi():
    return flask.render_template('incription_reussi.html', nom_user=flask.session['user'][0])

@app.route('/logout/', methods=['GET'])
def logout():
    flask.session.pop('user')
    flask.session.pop('pigeon')
    return flask.redirect(flask.url_for('accueil'))

@app.route('/subscription/', methods=['GET', 'POST'])
def subscription():
    if flask.request.method == 'POST':
        pseudo = flask.request.form['pseudo']
        mdp = flask.request.form["mdp"]
        mdp_confirme = flask.request.form["mdp_verifie"]
        Num_Etudiant = flask.request.form["Num_Etudiant"]
        if (mdp == mdp_confirme):
            query = ("INSERT INTO inscrit (pseudo, mdp, num_Etudiant) \
            VALUES (%s, %s, %s)")
            donnee = (pseudo, mdp, Num_Etudiant)
            curr.execute(query, donnee)
            conn.commit()
            #gestion de flask.session
            flask.session["user"] = donnee
            flask.session["pigeon"] = []
            return flask.redirect(flask.url_for('inscription_reussi'))

        # flask.flash fournit un moyen de donner un feedback à un utilisateur
        flask.flash("Les mots de passe ne sont pas identiques.")
        # permet de rediriger la personne sur le formulaire d'inscription
        return flask.render_template('inscription.html')
    else:
        return flask.render_template('inscription.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'POST':
        pseudo = flask.request.form['pseudo']
        mdp = flask.request.form['mdp']
        query = ("SELECT * FROM inscrit WHERE pseudo = %s and mdp = %s")
        donnee = (pseudo, mdp)
        curr.execute(query, donnee)
        donnee_table = curr.fetchall()
        if (len(donnee_table) > 0):
            flask.session["pigeon"] = []
            flask.session['user'] = donnee_table
            message_flash = "connection reussi "+donnee[0]
            flask.flash(message_flash)
            return flask.redirect(flask.url_for('accueil_mat'))

        flask.flash("Information incorectes")
        return flask.redirect(flask.url_for('subscription'))
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
    if flask.request.method == 'POST':
        cb1 = flask.request.form['num_cb1']
        if (not(verif(cb1))):
            flask.flash("numero de carte bleu invalide")
            return flask.render_template('form_cb.html')
        cb2 = flask.request.form['num_cb2']
        if (not(verif(cb2))):
            flask.flash("numero de carte bleu invalide")
            return flask.render_template('form_cb.html')
        cb3 = flask.request.form['num_cb3']
        if (not(verif(cb3))):
            flask.flash("numero de carte bleu invalide")
            return flask.render_template('form_cb.html')
        cb4 = flask.request.form['num_cb4']
        if (not(verif(cb4))):
            flask.flash("numero de carte bleu invalide")
            return flask.render_template('form_cb.html')
        crypt = flask.request.form['cryptogramme_visuel']
        if (not(verif(crypt))):
            flask.flash("cryptogramme visuel invalide")
            return flask.render_template('form_cb.html')
        annee = int(flask.request.form['annee'])
        if (annee == 2018):
            mois = int(flask.request.form['mois'])
            if (mois < 5):
                flask.flash("carte bleu invalide")
                return flask.render_template('form_cb.html')
    flask.flash("paiement effectué")
    update_table_stock()
    update_table_caution()
    flask.session["pigeon"] = []
    return flask.redirect(flask.url_for('accueil'))


@app.route('/catalogue/', methods=['GET', 'POST'])
def catalogue():
    query = ("SELECT intitule_materiel, quantite, prix_unite_hf \
    FROM materiel_stock, type_materiel \
    WHERE materiel_stock.Ref_Type_Materiel = type_materiel.Ref_Type_Materiel")
    curr.execute(query)
    donnee = curr.fetchall()
    if flask.request.method == 'POST':
        quantite_acheter = int(flask.request.form['quantite'])
        intitule_materiel = flask.request.form['intitule_materiel']
        prix_u_hf = int(flask.request.form['prix_u_hf'])
        quantite_total_commande = incrementation_pigeon(intitule_materiel,
                                                        quantite_acheter,
                                                        prix_u_hf)
        if (peut_acheter(donnee, intitule_materiel, quantite_total_commande)):
            flask.flash("ajout au panier")
        else:
            flask.flash("pas assez en stock")
            return flask.render_template("catalogue.html", pigeon=donnee,
                                   est_connecte=('user' in flask.session))
    return flask.render_template("catalogue.html", pigeon=donnee,
                           est_connecte=('user' in flask.session))


@app.route('/panier/', methods=['GET'])
def panier():
    # print("\n\n\n", flask.session["pigeon"], "\n\n\n")
    prix_tot = 0
    for i, article in enumerate(flask.session['pigeon']):
        j = 0
        while j < flask.session['pigeon'][i][1]:
            prix_tot = prix_tot + flask.session['pigeon'][i][2]
            j += 1
    return flask.render_template("panier.html", articles=flask.session["pigeon"], prix_total = prix_tot)


@app.route('/payer/', methods=['GET'])
def payer():
    return flask.render_template("form_cb.html")


if __name__ == '__main__':
    conn = connect()
    curr = conn.cursor()
    # oriente la recherche des table dans le schema
    curr.execute("SET SEARCH_PATH TO projeti63")
    app.secret_key = "bien chiant"
    app.run(debug=True)
