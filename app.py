from flask import Flask, render_template, request
import random
from database import *
from datetime import datetime

app = Flask(__name__)

class profiles():
    def __init__(self):
        self.options=["AA","AAwL","AT","ATwL","TA","TAwL","TT","TTwL"]
        self.choice=""
    def select(self):
        self.choice= random.choice(self.options) +".png"
        return self.choice

admin = database()

@app.route("/" , methods=['GET', 'POST'])
def hello_world():
    return render_template('dump.html', check="1")

@app.route("/demographics", methods=['GET', 'POST'])
def instruction():
    if request.method == 'POST':
        email=request.form['name']
        date= datetime.now().strftime("%d/%m/%Y")
        try:
            check=request.form['check']
        except:
            check="0"

        if check!="1":
            return render_template('dump.html',check="0")
        else:
            admin.insert({"Email":email ,"Date":date})

        return render_template('demographic.html', email=email)


@app.route("/instructions", methods=['GET', 'POST'])
def demog():
    if request.method == 'POST':
        email=request.form['Email']
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        orientation = request.form['sexual orientation']
        education = request.form['education']
        occupation = request.form['occupation']
        city = request.form['cityofresidence']
        status = request.form['currentrelationshipstatus']
        past = request.form['romantic past']
        datepast = request.form['app past']
        datepresent = request.form['app present']
        diagnosis = request.form['diagnosis']
        know = request.form['knowsomeone']
        data={"name":name, "age":age, "gender":gender, "sexual orientation":orientation, "education":education, "occupation":occupation, "city of residence":city, "current relationship status":status, "romantic past":past, "date past":datepast, "date present":datepresent, "has autism":diagnosis, "know someone":know}
        admin.update({"Email":email},data)
        return render_template('index.html', email=email)
    

@app.route("/show_profile", methods=['GET', 'POST'])
def print_about():
    if request.method=='POST':
        email = request.form['Email']
        obj=profiles()
        img= obj.select()
        choice = "./static/"+ img
        admin.update({"Email":email},{"img": img})
        return render_template('profile.html', img_url=choice, email=email)
    else:
        return render_template('index.html' ,email="Not Found")

@app.route("/dbq_instructions", methods=['GET', 'POST'])
def dbq_instruction():
    if request.method == 'POST':
        email = request.form['Email']
        return render_template('dbq_instructions.html', email=email)

@app.route("/dbq", methods=['GET', 'POST'])
def dbq():
    if request.method=='POST':
        email=request.form['Email']
        return render_template('dbq.html', email=email)

@app.route("/surveyone", methods=['GET', 'POST'])
def surveyone():
    if request.method == 'POST':
        op=['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty','twentyone','twentytwo','twentythree','twentyfour','twentyfive','twentysix','twentyseven','twentyeight','twentynine','thirty','thirtyone','thirtytwo','thirtythree','thirtyfour','thirtyfive','thirtysix','thirtyseven','thirtyeight','thirtynine','fourty','fourtyone','fourtytwo']
        q1=[request.form[i] for i in op]
        email=request.form['Email']
        admin.update({"Email":email}, {"DBQ":q1})
        #handle the results of the dbq
        return render_template('surveyone.html', email=email)

@app.route("/halt_screen", methods=['GET', 'POST'])
def halt():
    if request.method=='POST':
        autism=request.form['autism']
        email= request.form['Email']
        #handle the answer to autism check here
        admin.update({"Email":email},{"Autism":autism})
        return render_template("halt.html", email=email)

@app.route("/autism_survey", methods=['GET', 'POST'])
def autism_survey():
    if request.method=='POST':
        email=request.form['Email']
        return render_template("autism_survey.html", email=email)

@app.route("/thank_you", methods=['GET', 'POST'])
def thank_you():
    if request.method == 'POST':
        op=['one','two','three','four','five','six','seven','eight','nine','ten','eleven','tweleve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty','twentyone','twentytwo']
        q1=[request.form[i] for i in op]
        email=request.form['Email']
        admin.update({"Email":email},{"KKA":q1})

    return render_template("thank_you.html")

if __name__ == "__main__":
    app.run(debug=True)
