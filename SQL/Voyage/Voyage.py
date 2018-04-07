import flask
import psycopg2

app = flask.Flask(__name__)

param = "dbname='testpython' user='marc' host='localhost'"

try:
    conn = psycopg2.connect(param)
    print("\n connecté \n")
except:
    print("\nERREUR DE CO !!!\n")

curr = conn.cursor()

###################################################

@app.route('/', methods = ['POST','GET'])

def acueil():
    return flask.render_template('accueil.html')

###################################################

@app.route('/templates/form_voyage', methods = ['POST','GET'])

def n_voyage():
    return flask.render_template('form_voyage.html')

###################################################

@app.route('/templates/finir_entrer_voyage', methods = ['POST','GET'])

def fin_voy():
    if flask.request.method == 'POST':
# Les mots entre '' doivent correspondre à ceux entre "" dans le fichier entrer_voyage.html
        type_voy = flask.request.form['type']
        prix = flask.request.form['prix']
        t_transp = flask.request.form['t_transp']
#les mots après le .format doibent correspondre à ceux ecrit avant le = au dessus
        query = "INSERT into VOYAGE(type, prix, type_transport) Values ( \
        '{}', '{}', '{}');".format (type_voy, prix, t_transp)
        #execute la requete et met tout dans le buffer
        curr.execute(query)
        #sert à mettre ce qu'il y a dans le buffer dans la table
        conn.commit()  #mettre en commentaire jusque là
        #affiche à l'ecran les donnees qu'on a rentre
# Le result_... doit correspondre à celui dans le fichier perosnne.html
        return flask.render_template('finir_entrer_voyage.html',\
        result_type_voy = type_voy, result_prix = prix,\
        result_type_transp = t_transp)

###################################################

if __name__ == '__main__':
    app.run(debug=True)
