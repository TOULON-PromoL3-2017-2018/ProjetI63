import flask
import psycopg2

app = flask.Flask(__name__)

param = {'host': '10.9.185.1'}  # "dbname='testpython' user='marc'
# param = "host='localhost' dbname='testpython' user='marc' password='mdp'"

try:
    conn = psycopg2.connect(**param)
    # conn = psycopg2.connect(param)
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
        dest = flask.request.form['destination']
        type_voy = flask.request.form['type']
        prix = flask.request.form['prix']

        # les mots après le .format doibent correspondre à ceux ecrit avant
        # le = au dessus
        query = "INSERT into VOYAGE (num_responsable, num_organisateur, \
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

@app.route('/templates/form_responsable', methods=['POST', 'GET'])
def n_resp():
    return flask.render_template('form_responsable.html')

###################################################

@app.route('/templates/finir_responsable', methods=['POST', 'GET'])
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

@app.route('/templates/form_entre_loc', methods=['POST', 'GET'])
def n_entr_loc():
    return flask.render_template('form_entre_loc.html')

###################################################

@app.route('/templates/finir_entre_loc', methods=['POST', 'GET'])
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

@app.route('/templates/form_trajet', methods=['POST', 'GET'])
def n_trajet():
    return flask.render_template('form_trajet.html')

###################################################

@app.route('/templates/finir_trajet', methods=['POST', 'GET'])
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

@app.route('/templates/form_vehicule', methods=['POST', 'GET'])
def n_vehicule():
    return flask.render_template('form_vehicule.html')

###################################################

@app.route('/templates/finir_vehicule', methods=['POST', 'GET'])
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

@app.route('/templates/form_necessite', methods=['POST', 'GET'])
def n_association():
    return flask.render_template('form_necessite.html')

###################################################

@app.route('/templates/finir_necessite', methods=['POST', 'GET'])
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



if __name__ == '__main__':
    app.run(debug=True)

    # SQLAlchemy
    # initd.org/psycopg/docs/usage.html
