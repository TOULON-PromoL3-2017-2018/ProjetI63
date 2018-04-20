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

        query = "INSERT INTO Etudiant(nom_etudiant, prenom_etudiant, \
        date_naissance_etudiant, filiere_etudiant, tel_etudiant,\
        mail_etudiant, rue_etudiant, ville_etudiant, code_postal_etudiant, \
        membre_asso) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        data = (nom_etu, pre_etu, date_nais, filiere, tel_etu, mail_etu,
                rue_etu, ville_etu, code_post, mbr_asso)
        curr.execute(query, data)
        conn.commit()
        return flask.render_template('valid_insc.html', res_nom=nom_etu)

if __name__ == '__main__':

    app.run(debug=True)
