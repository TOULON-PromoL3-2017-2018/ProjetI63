import flask
import psycopg2

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

@app.route("/",  methods=["POST", "GET"])
@app.route("/evenement/", methods=["POST", "GET"])
def accueil():
    return flask.render_template('accueil.html')


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
    # si inscrit dans table de base ok sinon faire une erreur
    # donc renseigner num participant pour le mettre dans inscritequipe
    # donner num equipe comme identifiant
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
# faire import time et faire date = t.localtime() puis date[x] pour avoir les infos


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
        data = (NoPart)
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
        data = (NoPart)
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

# faire evenement et ce qui lui est associé

# demander pour compte admin sur site pour creer evenement la je fais juste
# la participation

app.run(debug=True)
