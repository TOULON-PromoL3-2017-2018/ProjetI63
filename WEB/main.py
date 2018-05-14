# -*- coding:utf-8 -*-

from __future__ import print_function
import time
import flask
import psycopg2
import smtplib
from datetime import datetime


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

@app.route('/', methods=['GET'])
def accueil_commun():
    return flask.render_template('accueil_commun.html')


@app.route('/accueil_etu/', methods=['POST', 'GET'])
def hello():
    return flask.render_template('accueil.html')


@app.route('/form_insc_etu/', methods=['POST', 'GET'])
def new_insc():
    return flask.render_template('form_insc_etu.html')


@app.route('/login_etu/', methods=['POST', 'GET'])
def new_insc_cpt():
    return flask.render_template('login_etu.html')


@app.route("/logout_etu/")
def logout_etu():
    session.pop("login", None)
    return redirect("/")


@app.route('/form_insc_subv/', methods=['POST', 'GET'])
def new_inscr():
    return flask.render_template('form_insc_subv.html')


@app.route('/valid_insc_etu/', methods=['POST', 'GET'])
def inscription():
    if flask.request.method == 'POST':
        nom_etu = flask.request.form['name_etu']
        pre_etu = flask.request.form['pren_etu']
        date_nais = flask.request.form['date']
        filiere = flask.request.form['fil']
        tel_etu = flask.request.form['tel']
        mail_etu = flask.request.form['mail']
        rue_etu = flask.request.form['rue']
        ville_etu = flask.request.form['town']
        code_post = flask.request.form['code']
        mbr_asso = flask.request.form['suceur']

        query = "INSERT INTO Etudiant(nom_etudiant, prenom_etudiant,\
        date_naissance_etudiant, filiere_etudiant, tel_etudiant,\
        mail_etudiant, rue_etudiant, ville_etudiant, code_postal_etudiant,\
        membre_asso) VALUES (%s, %s, to_date(%s, 'DD MM YYYY'), %s, %s, %s, %s,\
        %s, %s, %s);"
        data = (nom_etu, pre_etu, date_nais, filiere, tel_etu, mail_etu,
                rue_etu, ville_etu, code_post, mbr_asso)
        curr.execute(query, data)
        conn.commit()
        return flask.render_template('valid_insc_etu.html', res_nom=nom_etu)


@app.route('/valid_compte_etu/', methods=['POST', 'GET'])
def val_insc_cpt():
    if flask.request.method == 'POST':
        login = flask.request.form['log']
        mdp = flask.request.form['psw']
        number = flask.request.form['num']

        query = "INSERT INTO Comptes_membres(login, mdp, num_etudiant) VALUES \
        (%s, %s, %s);"
        data = (login, mdp, number)
        curr.execute(query, data)
        conn.commit()
        return flask.render_template('valid_compte_etu.html', log=login)


@app.route('/valid_insc_sub/', methods=['POST', 'GET'])
def inscription2():
    if flask.request.method == 'POST':
        nom_subv = flask.request.form['name_subv']
        rue_subv = flask.request.form['rue']
        ville_subv = flask.request.form['vil']
        code_subv = flask.request.form['code']
        tel_subv = flask.request.form['tel']
        nom_rep = flask.request.form['nom_rep']
        mail_rep = flask.request.form['mail']

        query = "INSERT INTO Subventionneurs(nom_subventionneur,\
        rue_subventionneur, ville_subventionneur, code_postal_subventionneur,\
        tel_subventionneur, nom_représentant, mail_représentant) VALUES (%s,\
        %s, %s, %s, %s, %s, %s);"
        data = (nom_subv, rue_subv, ville_subv, code_subv, tel_subv, nom_rep,
                mail_rep)
        curr.execute(query, data)
        conn.commit()
        return flask.render_template('valid_insc_sub.html', res_nom=nom_subv)


@app.route('/finances/', methods=['POST', 'GET'])
def finance():
    # return flask.render_template('finances.html', res_cpt=trigger de etat des
    #comptes)
    return flask.render_template('finances.html')


@app.route('/financements/', methods=['POST', 'GET'])
def financements():
    curr.execute("SELECT (num_demande_argent, montant, source,\
    validation) FROM Financement WHERE validation=1")
    return flask.render_template('financements.html')


# en attendant la mise en commun
# @app.route("/",  methods=["POST", "GET"])
@app.route("/evenement/", methods=["POST", "GET"])
def accueilev():
    return flask.render_template('accueilev.html')


@app.route("/evenement/formext/", methods=["POST", "GET"])
def formext():
    query = "SELECT NoUniversite, NomUniversite FROM Universite"
    curr.execute(query)
    rows = curr.fetchall()
    return flask.render_template('formext.html', Universites=rows)


@app.route("/evenement/inscritext/", methods=["POST", "GET"])
def inscritext():
    global noparticipant
    if flask.request.method == "POST":
        NoPart = noparticipant
        noparticipant += 1
        NumUniv = flask.request.form['NoUniv']
        Nom = flask.request.form['NomEtud']
        Prenom = flask.request.form['PrenomEtud']
        Email = flask.request.form['Mail']
        Telep = flask.request.form['Tel']
        NumEtud = flask.request.form['NoEtud']
        query = "INSERT INTO ParticipantAutre VALUES(%s ,%s, %s, %s, %s, %s,\
        %s)"
        data = (str(NoPart), NumUniv, Nom, Prenom, Email, Telep, NumEtud)
        curr.execute(query, data)
        conn.commit()
        return flask.render_template('inscritext.html', NoParti=NoPart)


@app.route("/evenement/formint/", methods=["POST", "GET"])
def formint():
    return flask.render_template('formint.html')


@app.route("/evenement/inscritint/", methods=["POST", "GET"])
def inscritint():
    # Ne fonctionne que quand j'aurais le lien avec Xavier
    global noparticipant
    if flask.request.method == "POST":
        NoPart = noparticipant
        noparticipant += 1
        NumUniv = "1"
        NumEtud = flask.request.form['NoEtud']
        query = "INSERT INTO ParticipantAsso VALUES(%s, %s, %s)"
        data = (str(NoPart), NumUniv, NumEtud)
        curr.execute(query, data)
        conn.commit()
        return flask.render_template('inscritint.html', NoParti=NoPart)


@app.route("/evenement/universite/", methods=["POST", "GET"])
def universite():
    query = "SELECT * FROM Universite"
    curr.execute(query)
    rows = curr.fetchall()
    return flask.render_template('universite.html', Universites=rows)


@app.route("/evenement/formuniv/", methods=["POST", "GET"])
def formuniv():
    return flask.render_template('formuniv.html')


@app.route("/evenement/inscrituniv/", methods=["POST", "GET"])
def inscrituniv():
    if flask.request.method == "POST":
        NomUniv = flask.request.form['NomU']
        Ville = flask.request.form['City']
        Rue = flask.request.form['Street']
        Arr = flask.request.form['Arrond']
        Cont = flask.request.form['Contact']
        query = "INSERT INTO Universite (NomUniversite, Ville, Rue,\
        Arrondissement, Contact) VALUES (%s, %s, %s, %s, %s)"
        data = (NomUniv, Ville, Rue, Arr, Cont)
        curr.execute(query, data)
        conn.commit()
        return flask.render_template('inscrituniv.html')


@app.route("/evenement/equipe/", methods=["POST", "GET"])
def equipe():
    query = "SELECT * FROM Equipe"
    curr.execute(query)
    rows = curr.fetchall()
    return flask.render_template('equipe.html', Equipes=rows)


@app.route("/evenement/formequipe/", methods=["POST", "GET"])
def formequipe():
    return flask.render_template('formequipe.html')


@app.route("/evenement/inscritequipe/", methods=["POST", "GET"])
def inscritequipe():
    if flask.request.method == "POST":
        NoPart = flask.request.form['NumPart']
        NomEq = flask.request.form['NomEquipe']
        query = "SELECT noparticipantautre FROM participantautre WHERE \
        noparticipantautre = %s"
        data = (NoPart,)
        curr.execute(query, data)
        rowother = curr.fetchall()
        if len(rowother) != 0:
            query = "INSERT INTO Equipe (NomEquipe) VALUES (%s)"
            data = (NomEq)
            curr.execute(query, data)
            conn.commit()
            query = "SELECT max(NumEquipe) FROM Equipe"
            curr.execute(query)
            res = curr.fetchall()
            NumEq = res[0][0]
            query = "INSERT INTO InscritEquipeAutre VALUES (%s, %s)"
            data = (NoPart, NumEq)
            curr.execute(query, data)
            conn.commit()
            return flask.render_template('inscritequipe.html', NomEqui=NomEq,\
                                         NumEqui=NumEq)
        query = "SELECT noparticipantasso FROM ParticipantAsso WHERE \
        noparticipantasso = %s"
        data = (NoPart)
        curr.execute(query, data)
        rowasso = curr.fetchall()
        if len(rowasso) != 0:
            query = "INSERT INTO Equipe (NomEquipe) VALUES (%s)"
            data = (NomEq,)
            curr.execute(query, data)
            conn.commit()
            query = "SELECT max(NumEquipe) FROM Equipe"
            curr.execute(query)
            res = curr.fetchall()
            NumEq = res[0][0]
            query = "INSERT INTO InscritEquipeAsso VALUES (%s, %s)"
            data = (NoPart, NumEq)
            curr.execute(query, data)
            conn.commit()
            return flask.render_template('inscritequipe.html', NomEqui=NomEq,\
                                         NumEqui=NumEq)
        return flask.render_template('erreurinscriteq.html', NoParti=NoPart)


@app.route("/evenement/formpart/", methods=["POST", "GET"])
def formpart():
    return flask.render_template('formpart.html')


@app.route("/evenement/inscritpart/", methods=["POST", "GET"])
def inscritpart():
    if flask.request.method == "POST":
        NoPart = flask.request.form['NumPart']
        NumEq = flask.request.form['NumEquipe']
        query = "SELECT noparticipantautre FROM participantautre WHERE \
        noparticipantautre = %s"
        data = (NoPart,)
        curr.execute(query, data)
        rowother = curr.fetchall()
        # verif si dans participantautre
        if len(rowother) != 0:
            query = "SELECT NumEquipe FROM Equipe WHERE NumEquipe = %s"
            data = (NumEq,)
            curr.execute(query, data)
            res = curr.fetchall()
            # verif si dans equipe
            if len(res) != 0:
                query = "INSERT INTO InscritEquipeAutre VALUES (%s, %s)"
                data = (NoPart, NumEq)
                curr.execute(query, data)
                conn.commit()
                return flask.render_template('inscritpart.html', NumEqui=NumEq)
            return flask.render_template('erreurequipe.html', NumEqui=NumEq)
        query = "SELECT noparticipantasso FROM ParticipantAsso WHERE \
        noparticipantasso = %s"
        data = (NoPart,)
        curr.execute(query, data)
        rowasso = curr.fetchall()
        # verif si dans participantasso
        if len(rowasso) != 0:
            query = "SELECT NumEquipe FROM Equipe WHERE NumEquipe = %s"
            data = (NumEq,)
            curr.execute(query, data)
            res = curr.fetchall()
            # verif si dans equipe
            if len(res) != 0:
                query = "INSERT INTO InscritEquipeAsso VALUES (%s, %s)"
                data = (NoPart, NumEq)
                curr.execute(query, data)
                conn.commit()
                return flask.render_template('inscritpart.html', NumEqui=NumEq)
            return flask.render_template('erreurequipe.html', NumEqui=NumEq)
        return flask.render_template('erreurinscriteq.html', NoParti=NoPart)


# juste participation pas d'édition avec ajout d'évènement
@app.route("/evenement/evenement/", methods=["POST", "GET"])
def evenement():
    return flask.render_template('evenement.html')


@app.route("/evenement/evenementpasse/", methods=["POST", "GET"])
def evenementpasse():
    todaydate = datetime.now()
    query = "SELECT noevenement, typeevenement, notation, dateevenement FROM \
            evenement NATURAL JOIN type WHERE dateevenement < %s"
    data = (todaydate,)
    curr.execute(query, data)
    rowevenpast = curr.fetchall()
    return flask.render_template('evenementpasse.html', Evpast=rowevenpast)


@app.route("/evenement/evenementfutur/", methods=["POST", "GET"])
def evenementfutur():
    todaydate = datetime.now()
    query = "SELECT noevenement, typeevenement, dateevenement, nomsport from \
    evenement natural join type left outer join (select * from \
    evenementsport natural join sport) as t on \
    evenement.noevenementsport = t.noevenementsport WHERE \
    dateevenement >= %s"
    data = (todaydate,)
    curr.execute(query, data)
    rowevenfutur = curr.fetchall()
    return flask.render_template('evenementfutur.html', Evfutur=rowevenfutur)


@app.route("/evenement/inscriptionevenement/", methods=["POST", "GET"])
def inscriptionevenement():
    return flask.render_template('inscriptionevenement.html')


@app.route("/evenement/forminscritev/", methods=["POST", "GET"])
def forminscritev():
    if flask.request.method == "POST":
        NoEv = flask.request.form['NumEven']
        todaydate = datetime.now()
        query = "SELECT noevenement FROM evenement WHERE dateevenement\
                > %s AND noevenement = %s"
        data = (todaydate, NoEv)
        curr.execute(query, data)
        row = curr.fetchall()
        # si evenement bien valide
        if len(row) != 0:
            # test si evenement sport et si oui si coll ou ind
            query = "SELECT noevenementsport FROM evenement WHERE noevenement =\
                    %s"
            data = (NoEv,)
            curr.execute(query, data)
            res = curr.fetchall()
            if res[0][0] == None:
                # si pas evenement sportif
                return flask.render_template('forminscritevind.html',
                                             NumEv=NoEv)
            noevsport = res[0][0]
            query = "SELECT typesport FROM evenementsport NATURAL JOIN \
                    sport WHERE noevenementsport = %s"
            data = (noevsport,)
            curr.execute(query, data)
            res = curr.fetchall()
            if res[0][0] == 'Individuel':
                return flask.render_template('forminscritevind.html',
                                             NumEv=NoEv)
            return flask.render_template('forminscriteveq.html', NumEv=NoEv)
        return flask.render_template('erreurevenement.html', NumEv=NoEv)


@app.route("/evenement/inscritevind/", methods=["POST", "GET"])
def inscritevind():
    if flask.request.method == "POST":
        NoEv = flask.request.form['NumEven']
        NoPart = flask.request.form['NumPart']
        query = "SELECT noparticipantautre FROM participantautre WHERE \
        noparticipantautre = %s"
        data = (NoPart,)
        curr.execute(query, data)
        rowother = curr.fetchall()
        # verif si dans participantautre
        if len(rowother) != 0:
            query = "INSERT INTO inscritautre VALUES (%s, %s)"
            data = (NoPart, NoEv)
            curr.execute(query, data)
            conn.commit()
            return flask.render_template('inscritevind.html', NumEv=NoEv)
        query = "SELECT noparticipantasso FROM ParticipantAsso WHERE \
        noparticipantasso = %s"
        data = (NoPart,)
        curr.execute(query, data)
        rowasso = curr.fetchall()
        # verif si dans participantasso
        if len(rowasso) != 0:
            query = "INSERT INTO inscritasso VALUES (%s, %s)"
            data = (NoPart, NoEv)
            curr.execute(query, data)
            conn.commit()
            return flask.render_template('inscritevind.html', NumEv=NoEv)
        return flask.render_template('erreurinscriteq.html', NoParti=NoPart)


@app.route("/evenement/inscriteveq/", methods=["POST", "GET"])
def inscriteveq():
    if flask.request.method == "POST":
        NoEv = flask.request.form['NumEven']
        NoEq = flask.request.form['NumEquipe']
        query = "SELECT NumEquipe FROM Equipe WHERE NumEquipe = %s"
        data = (NoEq,)
        curr.execute(query, data)
        res = curr.fetchall()
        # verif si dans equipe
        if len(res) != 0:
            query = "INSERT INTO inscritequipe VALUES (%s, %s)"
            data = (NoEq, NoEv)
            curr.execute(query, data)
            conn.commit()
            return flask.render_template('inscritevind.html', NumEv=NoEv)
        return flask.render_template('erreurequipe.html', NumEqui=NoEq)


@app.route("/evenement/classement/", methods=["POST", "GET"])
def classement():
    query = "SELECT nomsport FROM sport"
    curr.execute(query)
    res = curr.fetchall()
    return flask.render_template('classement.html', Sport=res)


@app.route("/evenement/afficheclass/", methods=["POST", "GET"])
def afficheclass():
    if flask.request.method == "POST":
        NomSp = flask.request.form['NomSport']
        query = "SELECT nomsport FROM sport WHERE nomsport = %s"
        data = (NomSp,)
        curr.execute(query, data)
        res = curr.fetchall()
        # verif si sport existe
        if len(res) != 0:
            # test si sport coll ou Individuel
            query = "SELECT typesport FROM sport WHERE nomsport = %s"
            data = (NomSp,)
            curr.execute(query, data)
            res = curr.fetchall()
            if res[0][0] == 'Individuel':
                query = "SELECT * FROM GagnantPers(%s)"
                curr.execute(query, data)
                res = curr.fetchall()
                return flask.render_template('afficheclass.html',
                                             NomSport=NomSp, Class=res)
            query = "SELECT * FROM GagnantEq(%s)"
            curr.execute(query, data)
            res = curr.fetchall()
            return flask.render_template('afficheclass.html',
                                         NomSport=NomSp, Class=res)
        return flask.render_template('erreursport.html', NomSport=NomSp)

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
    return flask.redirect(flask.url_for('accueil_commun'))

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
    return flask.redirect(flask.url_for('accueil_mat'))


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

@app.route('/voyage', methods=['POST', 'GET'])
def accueil_voy():
    return flask.render_template('accueil_voyage.html')

###################################################
###################################################
###################################################

@app.route('/voyage/form_voyageur', methods=['POST', 'GET'])
def n_voyageur():
    return flask.render_template('form_voyageur.html')

###################################################


@app.route('/voyage/finir_entrer_voyageur', methods=['POST', 'GET'])
def fin_voyageur():
    if flask.request.method == 'POST':
        # Les mots entre '' doivent correspondre à ceux entre "" dans le
        # fichier entrer_voyage.html
        num_voyageur = flask.request.form['num_v']
        du = flask.request.form['du']
        query = "INSERT into voyageur (num_voyageur, du) Values (%s, %s)"
        data = (num_voyageur, du)
        curr.execute(query, data)
        conn.commit()
        return flask.render_template('finir_entrer_voyageur.html',
                                     result_voyageur=num_voyageur,
                                     result_du=du)

###################################################
###################################################
###################################################

@app.route('/voyage/form_satisfaction', methods=['POST', 'GET'])
def n_satis():
    return flask.render_template('form_satisfaction.html')

###################################################


@app.route('/voyage/finir_satisfaction', methods=['POST', 'GET'])
def fin_satis():
    if flask.request.method == 'POST':
        # Les mots entre '' doivent correspondre à ceux entre "" dans le
        # fichier entrer_voyage.html
        sat = flask.request.form['s']
        num_voyageur = flask.request.form['num_v']
        num_voyage = flask.request.form['num_voy']
        query = "Update participe set satisfaction=(%s) where\
        num_voyageur=(%s) and num_voyage = (%s)"
        data = (sat, num_voyageur, num_voyage)
        curr.execute(query, data)
        conn.commit()
        return flask.render_template('finir_satisfaction.html',
                                     result_voyageur=num_voyageur,
                                     result_voyage=num_voyage,
                                     result_sat=sat)

###################################################
###################################################
###################################################

@app.route('/voyage/form_participe', methods=['POST', 'GET'])
def n_participation():
    return flask.render_template('form_participe.html')

###################################################


@app.route('/voyage/finir_participe', methods=['POST', 'GET'])
def fin_participation():
    if flask.request.method == 'POST':
        # Les mots entre '' doivent correspondre à ceux entre "" dans le
        # fichier entrer_voyage.html
        num_voyageur = flask.request.form['num_vr']
        num_voyage = flask.request.form['num_voy']
        nb_bag = flask.request.form['n_bag']
        query = "INSERT into Participe (num_voyageur, num_voyage,\
        nb_baggages) Values (%s, %s, %s)"
        # print(num_voyageur, num_voyage, nb_bag)
        data = (num_voyageur, num_voyage, nb_bag)
        curr.execute(query, data)
        conn.commit()
        return flask.render_template('finir_participe.html',
                                     result_voyageur=num_voyageur,
                                     result_voyage=num_voyage)


###################################################
###################################################
###################################################


@app.route('/voyage/form_voyage', methods=['POST', 'GET'])
def n_voyage():
    return flask.render_template('form_voyage.html')

###################################################


@app.route('/voyage/finir_entrer_voyage', methods=['POST', 'GET'])
def fin_voy():
    if flask.request.method == 'POST':
        # Les mots entre '' doivent correspondre à ceux entre "" dans le
        # fichier entrer_voyage.html
        num_responsable = flask.request.form['num_resp']
        num_organisateur = flask.request.form['num_org']
        dest = flask.request.form['destination']
        type_voy = flask.request.form['type']
        prix = flask.request.form['prix']

        # les mots après le .format doibent correspondre à ceux ecrit avant
        # le = au dessus
        query = "INSERT into VOYAGE (num_responsable, num_organisateur,\
        destination, type, prix) Values (%s, %s, %s, %s, %s);"
        # attention: data est un tuple !!
        data = (num_responsable, num_organisateur, dest, type_voy, prix)
        # execute la requete et met tout dans le buffer
        curr.execute(query, data)
        # sert à mettre ce qu'il y a dans le buffer dans la table
        conn.commit()
        # affiche à l'ecran les donnees qu'on a rentre
        return flask.render_template('finir_entrer_voyage.html',
                                     result_num_resp=num_responsable,
                                     result_num_org=num_organisateur,
                                     result_destination=dest,
                                     result_type_voy=type_voy,
                                     result_prix=prix)

###################################################
###################################################
###################################################


@app.route('/voyage/form_organisateur', methods=['Post', 'GET'])
def n_orga():
    return flask.render_template('form_organisateur.html')

###################################################


@app.route('/voyage/finir_organisateur', methods=['POST', 'GET'])
def fin_orga():
    if flask.request.method == 'POST':
        nom = flask.request.form['nom']
        prenom = flask.request.form['prenom']
        ville = flask.request.form['ville']
        code_ps = flask.request.form['c_p']
        rue = flask.request.form['rue']
        tel = flask.request.form['tel']
        mail = flask.request.form['mail']
        spe = flask.request.form['spe']

        query = "INSERT into organisateur (nom, prenom, ville, code_ps, rue,\
        tel, mail, specialisation) Values (%s, %s, %s, %s, %s, %s, %s, %s)"
        data = (nom, prenom, ville, code_ps, rue, tel, mail, spe)
        curr.execute(query, data)
        conn.commit()

        return flask.render_template('finir_organisateur.html',
                                     result_nom=nom, result_prenom=prenom,
                                     result_ville=ville,
                                     result_code_ps=code_ps,
                                     result_rue=rue, result_tel=tel,
                                     result_mail=mail, result_spe=spe)

###################################################
###################################################
###################################################

@app.route('/voyage/form_responsable', methods=['POST', 'GET'])
def n_resp():
    return flask.render_template('form_responsable.html')

###################################################

@app.route('/voyage/finir_responsable', methods=['POST', 'GET'])
def fin_resp():
    if flask.request.method == 'POST':
        nom = flask.request.form['nom']
        prenom = flask.request.form['prenom']
        tel = flask.request.form['tel']

        query = "INSERT into Responsable (nom_responsable, prenom_responsable,\
        tel_responsable) values (%s, %s, %s)"
        data = (nom, prenom, tel)
        curr.execute(query, data)
        conn.commit()
        return flask.render_template('finir_responsable.html',
                                     result_nom=nom, result_prenom=prenom,
                                     result_tel=tel)

###################################################
###################################################
###################################################

@app.route('/voyage/form_entre_loc', methods=['POST', 'GET'])
def n_entr_loc():
    return flask.render_template('form_entre_loc.html')

###################################################

@app.route('/voyage/finir_entre_loc', methods=['POST', 'GET'])
def fin_entr_loc():
    if flask.request.method == 'POST':
        nom = flask.request.form['nom']
        ville = flask.request.form['ville']
        code_ps = flask.request.form['c_ps']
        rue = flask.request.form['rue']
        tel = flask.request.form['tel']
        mail = flask.request.form['mail']

        query = "INSERT into entre_location (nom_entreprise, ville_entreprise,\
        code_ps_entreprise, rue_entreprise, tel_entreprise, mail_entreprise)\
        values (%s, %s, %s, %s, %s, %s)"
        data = (nom, ville, code_ps, rue, tel, mail)
        curr.execute(query, data)
        conn.commit()
        return flask.render_template('finir_entre_loc.html', result_nom=nom)

###################################################
###################################################
###################################################

@app.route('/voyage/form_trajet', methods=['POST', 'GET'])
def n_trajet():
    return flask.render_template('form_trajet.html')

###################################################

@app.route('/voyage/finir_trajet', methods=['POST', 'GET'])
def fin_trajet():
    if flask.request.method == 'POST':
        l_d = flask.request.form['lieu_dep']
        l_a = flask.request.form['lieu_arr']

        query = "INSERT into trajet (lieu_depart, lieu_arrive) values (%s, %s)"
        data = (l_d, l_a)
        curr.execute(query, data)
        conn.commit()
        return flask.render_template('finir_trajet.html', result_l_d=l_d,
                                     result_l_a=l_a)

###################################################
###################################################
###################################################

@app.route('/voyage/form_vehicule', methods=['POST', 'GET'])
def n_vehicule():
    return flask.render_template('form_vehicule.html')

###################################################

@app.route('/voyage/finir_vehicule', methods=['POST', 'GET'])
def fin_vehicule():
    if flask.request.method == 'POST':
        imm = flask.request.form['immatriculation']
        num_entr_loc = flask.request.form['n_e_l']
        type_v = flask.request.form['type']
        nb_places = flask.request.form['places']
        query = "INSERT into Vehicule (immatriculation, num_entre_location,\
        type_vehicule, nb_places) values (%s, %s, %s, %s)"
        data = (imm, num_entr_loc, type_v, nb_places)
        curr.execute(query, data)
        conn.commit()
        return flask.render_template('finir_vehicule.html', result_imm=imm,
                                     result_type=type_v)

###################################################
###################################################
###################################################

@app.route('/voyage/form_necessite', methods=['POST', 'GET'])
def n_association():
    return flask.render_template('form_necessite.html')

###################################################

@app.route('/voyage/finir_necessite', methods=['POST', 'GET'])
def fin_association():
    if flask.request.method == 'POST':
        num_traj = flask.request.form['n_t']
        num_voy = flask.request.form['n_v']
        sens = flask.request.form['s']
        dat_dep = flask.request.form['d_p']
        dat_arr = flask.request.form['d_a']
        heur_dep = flask.request.form['h_d']
        heur_arr = flask.request.form['h_a']
        prix = flask.request.form['prix']

        query = "INSERT into Necessite (num_trajet, num_voyage, sens,\
        date_depart, date_arrive, heure_depart, heure_arrive, prix_trajet)\
        values (%s, %s, %s, %s, %s, %s, %s, %s)"
        data = (num_traj, num_voy, sens, dat_dep, dat_arr, heur_dep, heur_arr, prix)
        curr.execute(query, data)
        conn.commit()
        return flask.render_template('finir_necessite.html', result_trajet=num_traj,
                                     result_voyage=num_voy)

###################################################
###################################################
###################################################

@app.route('/voyage/form_solicite', methods=['POST', 'GET'])
def n_solicite():
    return flask.render_template('form_solicite.html')

###################################################

@app.route('/voyage/finir_solicite', methods=['POST', 'GET'])
def fin_solicite():
    if flask.request.method == 'POST':
        num_traj = flask.request.form['n_t']
        imm = flask.request.form['imm']
        tel_chauf = flask.request.form['t_c']
        nb_pass = flask.request.form['n_p']
        nb_bag_max = flask.request.form['n_b_max']
        p_bag_max = flask.request.form['p_b_max']

        query = "INSERT into Solicite (num_trajet, immatriculation,\
        tel_chauffeur, nb_passagers, nb_baggages_max, poids_baggages_max)\
        values (%s, %s, %s, %s, %s, %s)"

        data = (num_traj, imm, tel_chauf, nb_pass, nb_bag_max, p_bag_max)
        curr.execute(query, data)
        conn.commit()
        return flask.render_template('finir_solicite.html', result_trajet=num_traj,
                                     result_imma=imm)

###################################################
###################################################
###################################################

@app.route('/voyage/liste_traitements')
def trait():
    return flask.render_template('liste_traitements.html')

###################################################

@app.route('/voyage/liste_voyage', methods=['POST', 'GET'])
def liste_voy():
    if flask.request.method == 'GET':
        query = "SELECT * from Voyage"
        curr.execute(query)
        var = curr.fetchall()
        return flask.render_template('liste_voyage.html', voyage=var)


###################################################

@app.route('/voyage/entrer_satisf', methods=['POST', 'GET'])
def satisf():
    id_voy = flask.request.form['id_n_v']
    return flask.render_template('entrer_satisf.html', result_sat=id_voy)


# fonction pour entrer la satisfaction d'un voyage
@app.route('/voyage/finir_satisf', methods=['POST', 'GET'])
def fin_sat():
    if flask.request.method == 'POST':
        voy = flask.request.form['id_n_v']
        voyageur = flask.request.form['id_voyageur']
        sat = flask.request.form['s']
        query = "UPDATE participe SET satisfaction=%s where num_voyageur=%s\
                 and num_voyage=%s"
        data = (sat, voyageur, voy)
        curr.execute(query, data)
        conn.commit()
        return flask.render_template('finir_satisf.html', result_voy=voy,
                                result_voyageur=voyageur, result_sat=sat)

###################################################

# fonction pour calculer la moyenne d'un voyage
@app.route('/voyage/consulter_note', methods=['POST', 'GET'])
def note():
    voy = flask.request.form['id_n_v']
    query = "SELECT satisfaction from participe where num_voyage=%s"
    data = (voy,)
    curr.execute(query, data)
    var = curr.fetchall()
    fin = len(var)
    i = 0
    moy = 0
    while i < fin:
        moy = moy + var[i][0]
        i = i + 1
    moy = moy / fin
    return flask.render_template('consulter_note.html', result_voy=voy, result_moy=moy)

###################################################

@app.route('/voyage/liste_voyage_note', methods=['POST', 'GET'])
def liste_voy_note():
    if flask.request.method == 'GET':
        query = "SELECT * from Voyage"
        curr.execute(query)
        var = curr.fetchall()
        return flask.render_template('liste_voyage_note.html', voyage=var)

@app.route('/log_success_etu/', methods=['POST', 'GET'])
def connexion_success():
    if flask.request.method == 'POST':
        login = flask.request.form['log']
        mdp = flask.request.form['psw']

        query = "SELECT * FROM Comptes_membres WHERE login = %s AND mdp = %s"
        data = (login, mdp)
        curr.execute(query, data)
        user = curr.fetchall()
        flask.session['user']=user
        return flask.render_template('log_success_etu.html', log=login)




if __name__ == '__main__':
    conn = connect()
    curr = conn.cursor()
    # oriente la recherche des table dans le schema
    curr.execute("SET SEARCH_PATH TO projeti63")

    query = "select max(noparticipantasso), max(noparticipantautre) from\
     participantasso, participantautre;"
    curr.execute(query)
    res = curr.fetchall()
    noun = res[0][0]
    nodeux = res[0][1]
    if (noun > nodeux):
        noparticipant = noun + 1
    else:
        noparticipant = nodeux + 1
    app.secret_key = "bien chiant"
    app.run(debug=True)
