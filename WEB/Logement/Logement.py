import flask
import psycopg2

app=flask.Flask(__name__)
#params={'host':'10.9.185.1'}

conn=psycopg2.connect(dbname='TB',user="kelly")#,password="pitsie1997")

cur=conn.cursor()


print("\n Co réussi !! \n")

cur.execute("SET SEARCH_PATH TO ProjetI63")

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
      query="INSERT INTO PROPRIETAIRE(nom_proprio,prenom_proprio,tel_proprio,adr_proprio) VALUES (%s,%s,%s,%s);"
      data=(nom,prenom,telephone,adr)
      cur.execute(query,data)
      conn.commit()
      #return '<form action="" method="post"><input type="text" name="name" /></form>'
      conn.commit()
      return flask.render_template("new_logement.html",nom=nom,prenom=prenom,adr=adr,telephone=telephone)
      


@app.route('/recap_annonce',methods = ['POST','GET'])
def recap_annonce():
  if flask.request.method == 'POST':

      cur.execute("SELECT nom_proprio,prenom_proprio,tel_proprio,adr_proprio FROM PROPRIETAIRE where num_proprio=(SELECT MAX(num_proprio) FROM PROPRIETAIRE);")
      rows=cur.fetchall()
      nom=rows[0][0]
      prenom=rows[0][1]
      telephone=rows[0][2]
      adr=rows[0][3]
    
      surface="{name}".format(name=flask.request.form['surf'])
      pieces="{name}".format(name=flask.request.form['pcs'])
      localisation="{name}".format(name=flask.request.form['lieu'])
      caution="{name}".format(name=flask.request.form['prix_caution'])
      loyer="{name}".format(name=flask.request.form['prix_loyer'])
      type_log="{name}".format(name=flask.request.form['choix'])
      prest="{name}".format(name=flask.request.form['choix_prest'])
      service="{name}".format(name=flask.request.form['choix_serv'])

      query="INSERT INTO LOGEMENT(type_logement,surface_logement,nb_pieces,localisation,montant_caution,montant_loyer) VALUES (%s,%s,%s,%s,%s,%s);"#, ('Maison',23,3,'toulon','Meublé',12,13)
      data=(type_log,surface,pieces,localisation,caution,loyer)
      cur.execute(query,data)
      conn.commit()
      
      return flask.render_template("recap_annonce.html",nom=nom,prenom=prenom,adr=adr,telephone=telephone,type_log=type_log,surface=surface,pieces=pieces,localisation=localisation,\
      caution=caution,loyer=loyer)#,prestation=prestation,service=service)

@app.route('/recherche_logement',methods = ['POST','GET'])
def recherche_logement():
  if flask.request.method == 'POST':

      """cur.execute("SELECT num_proprio FROM PROPRIETAIRE;")
      nums=cur.fetchall()
      print(nums)

      for annonce in nums:"""
          

      cur.execute("SELECT nom_proprio,prenom_proprio,tel_proprio,adr_proprio FROM PROPRIETAIRE where num_proprio=(SELECT MAX(num_proprio) FROM PROPRIETAIRE);")
      rows=cur.fetchall()
      nom=rows[0][0]
      prenom=rows[0][1]
      telephone=rows[0][2]
      adr=rows[0][3]
    
      cur.execute("SELECT type_logement,surface_logement,nb_pieces,localisation,prestations,montant_caution,montant_loyer FROM LOGEMENT where num_proprio=(SELECT MAX(num_proprio) FROM PROPRIETAIRE);")
      rows=cur.fetchall()
      print(rows)
      type_log=rows[0][0]
      surface=rows[0][1]
      pieces=rows[0][2]
      localisation=rows[0][3]

      cur.execute("SELECT prestations,montant_caution,montant_loyer FROM LOGEMENT where num_proprio=(SELECT MAX(num_proprio) FROM PROPRIETAIRE);")
      rows=cur.fetchall()
      print(rows)
      prestation=rows[0][0]
      caution=rows[0][1]
      loyer=rows[0][2]
      


      return flask.render_template("recherche_logement.html",nom=nom,prenom=prenom,adr=adr,telephone=telephone,type_log=type_log,surface=surface,pieces=pieces,localisation=localisation,caution=caution,prestation=prestation,loyer=loyer)



app.run(debug=True)



