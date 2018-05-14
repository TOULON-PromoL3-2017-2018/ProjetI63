import flask
import psycopg2

app = flask.Flask(__name__)

param = {'host': '10.9.185.1'}  # "dbname='testpython' user='username'
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
@app.route('/voyage', methods=['POST', 'GET'])
def accueil():
    return flask.render_template('accueil.html')

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




if __name__ == '__main__':
    app.run(debug=True)

    # SQLAlchemy
    # initd.org/psycopg/docs/usage.html
