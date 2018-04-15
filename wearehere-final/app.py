from flask import Flask, render_template, flash, request, jsonify, session, url_for
#from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

#from flask.ext.redis import Redis
import redis
import json
import requests 
import sys
import pyrebase
import re 

import models as dbHandler
import sqlite3

app = Flask(__name__)

#app.config['APPLICATION_ROOT'] = 'file:///Users/chinmayeehota/Desktop/HackDarthmouth2018/HereForYou/wearehere-master/templates/'
#app.config['SERVER_NAME'] = 'file:///Users/chinmayeehota/Desktop/HackDarthmouth2018/HereForYou/wearehere-master/templates/index.html'
#app.config['SERVER_NAME'] = 'myappname:5000'
#db = sqlite3.connect('wearehere.db')

#db = create_engine('sqlite:///wearehere.db')

#db.execute('CREATE TABLE records (user_name TEXT, perp_name TEXT, perp_descrip TEXT, location TEXT, inc_date TEXT, inc_time TEXT, incident TEXT, contact TEXT, nocontact TEXT, talk TEXT, legal TEXT)')
#db.close()



#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///Users/chinmayeehota/Desktop/HackDarthmouth2018/HereForYou/wearehere-master//Users/chinmayeehota/Desktop/HackDarthmouth2018/HereForYou/wearehere.db'
#db = SQLAlchemy(app)

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    
    if request.method == 'POST':
        user_name = request.form['user_name']
        perp_name = request.form['perp_name']
        perp_descrip = request.form['perp_descrip']
        location = request.form['location']
        inc_date = request.form['date']
        inc_time = request.form['time']
        incident = request.form['incident']
        contact = request.form['contact']
        dbHandler.insertUser(user_name, perp_name, perp_descrip, location, inc_date, inc_time, incident, contact)
        return render_template('submit.html')



@app.route("/aware", methods=['GET','POST'])
def aware():
    return render_template('aware.html')




@app.route("/resources", methods=['GET','POST'])
def resources():
    return render_template('resources.html')

@app.route("/immediate", methods=['GET','POST'])
def immediate():
    return render_template('immediate.html')

@app.route("/involve", methods=['GET','POST'])
def involve():
    return render_template('involve.html')


@app.route("/about", methods=['GET','POST'])
def about():
    return render_template('about.html')

'''
@app.route("/submit", methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        user_name = request.form['user_name']
        perp_name = request.form['perp_name']
        perp_descrip = request.form['perp_descrip']
        location = request.form['location']
        inc_date = request.form['date']
        inc_time = request.form['time']
        incident = request.form['incident']
        contact = request.form['contact']
        nocontact = request.form['nocontact']
        talk = request.form['talk']
        legal = request.form['legal']
        with sql.connect("wearehere.db") as db:
            c = db.cursor()
            c.execute("INSERT INTO records (user_name, perp_name , perp_descrip, location, inc_date, inc_time, incident, contact, nocontact, talk, legal) VALUES (?,?,?,?)",(user_name, perp_name , perp_descrip, location, inc_date, inc_time, incident, contact, nocontact, talk, legal))
            db.commit()
            db.close()
        return render_template('submit.html')

with app.test_request_context():
    print url_for('insert')
'''

if __name__ == "__main__":
    app.run(debug=True)