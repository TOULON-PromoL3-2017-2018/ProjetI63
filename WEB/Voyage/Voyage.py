import flask
import psycopg2

app = flask.Flask(__name__)

param = {'host': '10.9.185.1'}  # "dbname='testpython' user='marc'

try:
    conn = psycopg2.connect(**param)
    print("\n connecté \n")
except:
    print("\nERREUR DE CO !!!\n")

curr = conn.cursor()

###################################################


@app.route('/', methods=['POST', 'GET'])
def accueil():
    return flask.render_template('accueil.html')

###################################################
###################################################
###################################################


@app.route('/templates/form_voyage', methods=['POST', 'GET'])
def n_voyage():
    return flask.render_template('form_voyage.html')

###################################################


@app.route('/templates/finir_entrer_voyage', methods=['POST', 'GET'])
def fin_voy():
    if flask.request.method == 'POST':
        # Les mots entre '' doivent correspondre à ceux entre "" dans le
        # fichier entrer_voyage.html
        num_responsable = flask.request.form['num_resp']
        num_organisateur = flask.request.form['num_org']
        type_voy = flask.request.form['type']
        prix = flask.request.form['prix']
        t_transp = flask.request.form['t_transp']

        # les mots après le .format doibent correspondre à ceux ecrit avant
        # le = au dessus
        query = "INSERT into VOYAGE (num_responsable, num_organisateur, \
        type, prix, type_transport) Values (%s, %s, %s, %s, %s);"
        # attention: data est un tuple !!
        data = (num_responsable, num_organisateur, type_voy, prix, t_transp)
        # execute la requete et met tout dans le buffer
        curr.execute(query, data)
        # sert à mettre ce qu'il y a dans le buffer dans la table
        conn.commit()
        # affiche à l'ecran les donnees qu'on a rentre
        # Le result_... doit correspondre à celui dans le fichier perosnne.html
        return flask.render_template('finir_entrer_voyage.html',
                                     result_num_resp=num_responsable,
                                     result_num_org=num_organisateur,
                                     result_type_voy=type_voy,
                                     result_prix=prix,
                                     result_type_transp=t_transp)

###################################################
###################################################
###################################################


@app.route('/templates/form_organisateur', methods=['Post', 'GET'])
def n_orga():
    return flask.render_template('form_organisateur.html')

###################################################


@app.route('/templates/finir_organisateur', methods=['POST', 'GET'])
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

# @app.route('templates/form')

if __name__ == '__main__':
    app.run(debug=True)

    # SQLAlchemy
    # initd.org/psycopg/docs/usage.html
