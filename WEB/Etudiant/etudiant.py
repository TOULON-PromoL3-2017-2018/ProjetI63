import flask
import psycopg2

app = flask.Flask(__name__)
param = {'host': '10.9.185.1'}

try:
    conn = psycopg2.connect(**param)
    print("\nBien connecté\n")
except:
    print("\nERREUR DE CO !!!\n")

curr = conn.cursor()
# Me permet d'orienter la recherche des tables dans le schema !
curr.execute("SET SEARCH_PATH TO projeti63")


@app.route('/', methods=['POST', 'GET'])
def hello():
    return flask.render_template('accueil.html')


@app.route('/form_insc_etu/', methods=['POST', 'GET'])
def new_insc():
    return flask.render_template('form_insc_etu.html')


@app.route('/form_insc_subv/', methods=['POST', 'GET'])
def new_inscr():
    return flask.render_template('form_insc_subv.html')


@app.route('/valid_insc/', methods=['POST', 'GET'])
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
        membre_asso) VALUES (%s, %s, to_date(%s, 'DD MM YYYY'), %s, %s, %s, %s, %s, %s, %s);"
        data = (nom_etu, pre_etu, date_nais, filiere, tel_etu, mail_etu,
                rue_etu, ville_etu, code_post, mbr_asso)
        curr.execute(query, data)
        conn.commit()
        return flask.render_template('valid_insc.html', res_nom=nom_etu)


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


if __name__ == '__main__':

    app.run(debug=True)
