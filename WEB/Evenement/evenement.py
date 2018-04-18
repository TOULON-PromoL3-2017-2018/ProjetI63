import flask
import psycopg2

app = flask.Flask(__name__)
params = {
  'host': '10.9.185.1'
}
conn = psycopg2.connect(**params)
cur = conn.cursor()

#redemarre à 1 a chaque lancement donc le faire par fichier !!!!
#et ecrire chaque changement dans le fichier via fonction !!!!
noparticipant = 11

@app.route("/", methods = ["POST", "GET"])
def accueil():
    return flask.render_template('accueil.html')

@app.route("/formext/", methods = ["POST", "GET"])
def formext():
    query = "SELECT NoUniversite, NomUniversite FROM Universite"
    cur.execute(query)
    rows = cur.fetchall()
    return flask.render_template('formext.html', Universites = rows)

@app.route("/inscritext/", methods = ["POST","GET"])
def inscritext():
    global noparticipant
    if flask.request.method == "POST":
        NoPart = noparticipant
        noparticipant += 1
        #balance la fonction pour ecrire changement
        NumUniv = flask.request.form['NoUniv']
        Nom = flask.request.form['NomEtud']
        Prenom = flask.request.form['PrenomEtud']
        Email = flask.request.form['Mail']
        Telep = flask.request.form['Tel']
        NumEtud = flask.request.form['NoEtud']
        query = "INSERT INTO ParticipantAutre VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format\
        (NoPart, NumUniv, Nom, Prenom, Email, Telep, NumEtud)
        cur.execute(query)
        conn.commit()
        return flask.render_template("inscritext.html", NoParti = NoPart)

#Faire inscription interne et donner num participant

app.run(debug=True)
