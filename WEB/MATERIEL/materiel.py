import flask
import psycopg2

app = flask.Flask(__name__)
param = {'host': '127.0.0.1'}

try:
    conn = psycopg2.connect(**param)
    print("\n connecté")
except:
    print("\n erreur de connection")
    exit(1)

cur = conn.cursor()
# orieente la recherche des table dans le schema
curr.execute("SET SEARCH_PATH TO asso")

@app.route('/subscription/', methods=['GET', 'POST'])
def subscription():
    if request.method == 'POST':
        pseudo = flask.request.form['pseudo']
        mdp = request.form["mdp"]
        mdpConfC = request.form["mdp_vérifié"]
        if (mdpC == mdpConfC):
            query = "INSERT INTO inscrit(pseudo, mdp, Num_Etudiant) VALUES (%s, %s, %d);"
            cur.execute(query)
            conn.commit()
        flash("Les mots de passe ne sont pas identiques.")
        return redirect(url_for('inscription'))
    else:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)
