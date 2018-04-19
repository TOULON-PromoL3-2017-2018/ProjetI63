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

@app.route('/emprunt',methods = ['POST', 'GET'])
def emprunt():
  #if flask.request.method == 'GET':

  return flask.render_template("emprunt.html")
app.run(debug=True)
