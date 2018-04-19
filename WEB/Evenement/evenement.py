import flask
import psycopg2

app = flask.Flask(__name__)
params = {
  'host': '10.9.185.1'
}
conn = psycopg2.connect(**params)
cur = conn.cursor()

query = "select max(noparticipantasso), max(noparticipantautre) from participantasso, participantautre;"
cur.execute(query)
res = cur.fetchall()
noun = res[0][0]
nodeux = res[0][1]
if (noun > nodeux):
    noparticipant = noun + 1;
else:
    noparticipant = nodeux + 1;

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
        NumUniv = flask.request.form['NoUniv']
        Nom = flask.request.form['NomEtud']
        Prenom = flask.request.form['PrenomEtud']
        Email = flask.request.form['Mail']
        Telep = flask.request.form['Tel']
        NumEtud = flask.request.form['NoEtud']
        query = "INSERT INTO ParticipantAutre VALUES(%s ,%s, %s, %s, %s, %s, %s)"
        data = (str(NoPart), NumUniv, Nom, Prenom, Email, Telep, NumEtud)
        cur.execute(query, data)
        conn.commit()
        return flask.render_template("inscritext.html", NoParti = NoPart)

#Faire inscription interne et donner num participant

app.run(debug=True)
