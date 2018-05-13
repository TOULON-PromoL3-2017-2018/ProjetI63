import flask
import psycopg2
from datetime import datetime


app = flask.Flask(__name__)
params = {
  'host': '10.9.185.1'
}
conn = psycopg2.connect(**params)
cur = conn.cursor()

query = "select max(noparticipantasso), max(noparticipantautre) from\
 participantasso, participantautre;"
cur.execute(query)
res = cur.fetchall()
noun = res[0][0]
nodeux = res[0][1]
if (noun > nodeux):
    noparticipant = noun + 1
else:
    noparticipant = nodeux + 1

# en attendant la mise en commun
@app.route("/",  methods=["POST", "GET"])
@app.route("/evenement/", methods=["POST", "GET"])
def accueil():
    return flask.render_template('accueilev.html')


@app.route("/evenement/formext/", methods=["POST", "GET"])
def formext():
    query = "SELECT NoUniversite, NomUniversite FROM Universite"
    cur.execute(query)
    rows = cur.fetchall()
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
        cur.execute(query, data)
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
        cur.execute(query, data)
        conn.commit()
        return flask.render_template('inscritint.html', NoParti=NoPart)


@app.route("/evenement/universite/", methods=["POST", "GET"])
def universite():
    query = "SELECT * FROM Universite"
    cur.execute(query)
    rows = cur.fetchall()
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
        cur.execute(query, data)
        conn.commit()
        return flask.render_template('inscrituniv.html')


@app.route("/evenement/equipe/", methods=["POST", "GET"])
def equipe():
    query = "SELECT * FROM Equipe"
    cur.execute(query)
    rows = cur.fetchall()
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
        cur.execute(query, data)
        rowother = cur.fetchall()
        if len(rowother) != 0:
            query = "INSERT INTO Equipe (NomEquipe) VALUES (%s)"
            data = (NomEq)
            cur.execute(query, data)
            conn.commit()
            query = "SELECT max(NumEquipe) FROM Equipe"
            cur.execute(query)
            res = cur.fetchall()
            NumEq = res[0][0]
            query = "INSERT INTO InscritEquipeAutre VALUES (%s, %s)"
            data = (NoPart, NumEq)
            cur.execute(query, data)
            conn.commit()
            return flask.render_template('inscritequipe.html', NomEqui=NomEq,\
                                         NumEqui=NumEq)
        query = "SELECT noparticipantasso FROM ParticipantAsso WHERE \
        noparticipantasso = %s"
        data = (NoPart)
        cur.execute(query, data)
        rowasso = cur.fetchall()
        if len(rowasso) != 0:
            query = "INSERT INTO Equipe (NomEquipe) VALUES (%s)"
            data = (NomEq,)
            cur.execute(query, data)
            conn.commit()
            query = "SELECT max(NumEquipe) FROM Equipe"
            cur.execute(query)
            res = cur.fetchall()
            NumEq = res[0][0]
            query = "INSERT INTO InscritEquipeAsso VALUES (%s, %s)"
            data = (NoPart, NumEq)
            cur.execute(query, data)
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
        cur.execute(query, data)
        rowother = cur.fetchall()
        # verif si dans participantautre
        if len(rowother) != 0:
            query = "SELECT NumEquipe FROM Equipe WHERE NumEquipe = %s"
            data = (NumEq,)
            cur.execute(query, data)
            res = cur.fetchall()
            # verif si dans equipe
            if len(res) != 0:
                query = "INSERT INTO InscritEquipeAutre VALUES (%s, %s)"
                data = (NoPart, NumEq)
                cur.execute(query, data)
                conn.commit()
                return flask.render_template('inscritpart.html', NumEqui=NumEq)
            return flask.render_template('erreurequipe.html', NumEqui=NumEq)
        query = "SELECT noparticipantasso FROM ParticipantAsso WHERE \
        noparticipantasso = %s"
        data = (NoPart,)
        cur.execute(query, data)
        rowasso = cur.fetchall()
        # verif si dans participantasso
        if len(rowasso) != 0:
            query = "SELECT NumEquipe FROM Equipe WHERE NumEquipe = %s"
            data = (NumEq,)
            cur.execute(query, data)
            res = cur.fetchall()
            # verif si dans equipe
            if len(res) != 0:
                query = "INSERT INTO InscritEquipeAsso VALUES (%s, %s)"
                data = (NoPart, NumEq)
                cur.execute(query, data)
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
    cur.execute(query, data)
    rowevenpast = cur.fetchall()
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
    cur.execute(query, data)
    rowevenfutur = cur.fetchall()
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
        cur.execute(query, data)
        row = cur.fetchall()
        # si evenement bien valide
        if len(row) != 0:
            # test si evenement sport et si oui si coll ou ind
            query = "SELECT noevenementsport FROM evenement WHERE noevenement =\
                    %s"
            data = (NoEv,)
            cur.execute(query, data)
            res = cur.fetchall()
            if res[0][0] == None:
                # si pas evenement sportif
                return flask.render_template('forminscritevind.html',
                                             NumEv=NoEv)
            noevsport = res[0][0]
            query = "SELECT typesport FROM evenementsport NATURAL JOIN \
                    sport WHERE noevenementsport = %s"
            data = (noevsport,)
            cur.execute(query, data)
            res = cur.fetchall()
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
        cur.execute(query, data)
        rowother = cur.fetchall()
        # verif si dans participantautre
        if len(rowother) != 0:
            query = "INSERT INTO inscritautre VALUES (%s, %s)"
            data = (NoPart, NoEv)
            cur.execute(query, data)
            conn.commit()
            return flask.render_template('inscritevind.html', NumEv=NoEv)
        query = "SELECT noparticipantasso FROM ParticipantAsso WHERE \
        noparticipantasso = %s"
        data = (NoPart,)
        cur.execute(query, data)
        rowasso = cur.fetchall()
        # verif si dans participantasso
        if len(rowasso) != 0:
            query = "INSERT INTO inscritasso VALUES (%s, %s)"
            data = (NoPart, NoEv)
            cur.execute(query, data)
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
        cur.execute(query, data)
        res = cur.fetchall()
        # verif si dans equipe
        if len(res) != 0:
            query = "INSERT INTO inscritequipe VALUES (%s, %s)"
            data = (NoEq, NoEv)
            cur.execute(query, data)
            conn.commit()
            return flask.render_template('inscritevind.html', NumEv=NoEv)
        return flask.render_template('erreurequipe.html', NumEqui=NoEq)


@app.route("/evenement/classement/", methods=["POST", "GET"])
def classement():
    query = "SELECT nomsport FROM sport"
    cur.execute(query)
    res = cur.fetchall()
    return flask.render_template('classement.html', Sport=res)


@app.route("/evenement/afficheclass/", methods=["POST", "GET"])
def afficheclass():
    if flask.request.method == "POST":
        NomSp = flask.request.form['NomSport']
        query = "SELECT nomsport FROM sport WHERE nomsport = %s"
        data = (NomSp,)
        cur.execute(query, data)
        res = cur.fetchall()
        # verif si sport existe
        if len(res) != 0:
            # test si sport coll ou Individuel
            query = "SELECT typesport FROM sport WHERE nomsport = %s"
            data = (NomSp,)
            cur.execute(query, data)
            res = cur.fetchall()
            if res[0][0] == 'Individuel':
                query = "SELECT * FROM GagnantPers(%s)"
                cur.execute(query, data)
                res = cur.fetchall()
                return flask.render_template('afficheclass.html',
                                             NomSport=NomSp, Class=res)
            query = "SELECT * FROM GagnantEq(%s)"
            cur.execute(query, data)
            res = cur.fetchall()
            return flask.render_template('afficheclass.html',
                                         NomSport=NomSp, Class=res)
        return flask.render_template('erreursport.html', NomSport=NomSp)


# manque traitement si déjà inscrit donc risque de bug
app.run(debug=True)
