import flask
import psycopg2

app = flask.Flask(__name__)
params = {'host': '10.9.185.1'}

conn = psycopg2.connect(**params)
cur = conn.cursor()


@app.route('/')
def accueil():
    return flask.render_template('Accueil_Logement.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if flask.request.method == 'POST':

        conn.commit()

        return flask.render_template("result.html")


@app.route('/new_logement', methods=['POST', 'GET'])
def new_logement():
    if flask.request.method == 'POST':
        nom = "{name}".format(name=flask.request.form['name'])
        prenom = "{name}".format(name=flask.request.form['prename'])
        adr = "{name}".format(name=flask.request.form['adresse'])
        telephone = "{name}".format(name=flask.request.form['tel'])
        # return '<form action="" method="post"><input type="text" name="name"\
        # /></form>'
        return flask.render_template("new_logement.html", nom=nom,
                                     prenom=prenom, adr=adr,
                                     telephone=telephone)


@app.route('/enregistrement_logement', methods=['POST', 'GET'])
def enregistrement_logement():
    if flask.request.method == 'POST':
        surface = "{name}".format(name=flask.request.form['surf'])
        pieces = "{name}".format(name=flask.request.form['pcs'])
        localisation = "{name}".format(name=flask.request.form['lieu'])
        caution = "{name}".format(name=flask.request.form['prix_caution'])
        loyer = "{name}".format(name=flask.request.form['prix_loyer'])
        type_log = "{name}".format(name=flask.request.form['choix'])

        # return '<form action="" method="post"><input type="text" name="name"\
        # /></form>'
        return flask.render_template("enregistrement_logement.html",
                                     type_log=type_log, surface=surface,
                                     pieces=pieces, localisation=localisation,
                                     caution=caution, loyer=loyer)


app.run(debug=True)
