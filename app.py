import yaml
import re
from datetime import datetime
from flask import Flask
from datetime import datetime
from flask import make_response
from flask import request
from flask import Flask, render_template
from flask import abort
from flask import redirect
from flask.ext.bootstrap import Bootstrap 
from flask_wtf import FlaskForm
from flask.ext.uploads import UploadSet, configure_uploads, IMAGES
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap=Bootstrap(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500

# database configuration
db=yaml.load(open('db.yaml'))
app.config['MYSQL_HOST']= db['mysql_host']
app.config['MYSQL_USER']= db['mysql_user']
app.config['MYSQL_PASSWORD']= db['mysql_password']
app.config['MYSQL_DB']= db['mysql_db']

mysql = MySQL(app)
@app.route('/registration',methods=['GET','POST'])
def index():
      if request.method == 'POST':
    
              insertDetails=request.form
              name=insertDetails['name']
              username=insertDetails['user']
              password=insertDetails['pass']
              bdate=insertDetails['bdate']
              s1=insertDetails['s1']
              s2=insertDetails['s2']
              s3=insertDetails['s3']
              s4=insertDetails['s4']
              s5=insertDetails['s5']
              cur= mysql.connection.cursor()
              cur.execute("INSERT INTO login(username,password) VALUES(%s,%s)",(username,password,))
              cur.execute("INSERT INTO student(name,username,password,bdate,s1,s2,s3,s4,s5) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(name,username,password,bdate,s1,s2,s3,s4,s5,))
              mysql.connection.commit()
              cur.close()
              return redirect('/login')
      return render_template('registrationForm.html')
           
@app.route('/login',methods=['GET','POST'])
def search():       
       if request.method == 'POST':
          if request.form['action']=='login':
       	       searchDetails=request.form
       	       username=searchDetails['user']
               password=searchDetails['pass']
       	       cur= mysql.connection.cursor()
       	       resultValue=cur.execute("SELECT * FROM login WHERE username = %s AND password = %s",(username,password,))
               if resultValue > 0:
                   data=cur.fetchall()
                   return render_template('view.html',data=data)
               else:
                    return render_template('loginForm.html')
          elif request.form['action']=='registration':
               return redirect('/registration')  
              
       return render_template('loginForm.html')
if __name__ == '__main__':
     app.run(debug=True)

