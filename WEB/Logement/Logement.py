import flask
import psycopg2

app=flask.Flask(__name__)
params={'host':'10.9.185.1'}

conn=psycopg2.connect(**params)
cur=conn.cursor()
@app.route('/')
def accueil():
    return flask.render_template('Accueil_Logement.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if flask.request.method == 'POST':

      conn.commit()

      return flask.render_template("result.html")

@app.route('/new_logement',methods = ['POST', 'GET'])
def new_logement():
  if flask.request.method == 'POST':
      nom="{name}".format(name=flask.request.form['name'])
      prenom="{name}".format(name=flask.request.form['prename'])
      adr="{name}".format(name=flask.request.form['adresse'])
      telephone="{name}".format(name=flask.request.form['tel'])
      #return '<form action="" method="post"><input type="text" name="name" /></form>'
      return flask.render_template("new_logement.html",nom=nom,prenom=prenom,adr=adr,telephone=telephone)
app.run(debug=True)
