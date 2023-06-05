from flask import Flask, render_template, request
import random
from datetime import datetime

app = Flask(__name__)

class profiles():
    def __init__(self):
        self.options=["AA","AAwL","AT","ATwL","TA","TAwL","TT","TTwL"]
        self.choice=""
    def select(self):
        self.choice= random.choice(self.options) +".png"
        return self.choice


@app.route("/" , methods=['GET', 'POST'])
def hello_world():
    return render_template('dump.html', check="1")

@app.route("/instructions", methods=['GET', 'POST'])
def instruction():
    if request.method == 'POST':
        name=request.form['name']
        date= datetime.now().strftime("%d/%m/%Y")
        try:
            check=request.form['check']
        except:
            check="0"

        if check!="1":
            return render_template('dump.html',check="0")
        else:
            pass
            #handle the name and consent date here!

    return render_template('index.html')

@app.route("/show_profile", methods=['GET', 'POST'])
def print_about():
    obj=profiles()
    choice = "./static/"+ obj.select()
    return render_template('profile.html', img_url=choice)

@app.route("/dbq_instructions", methods=['GET', 'POST'])
def dbq_instruction():
    if request.method == 'POST':
        img = request.form['img_choice']
        #this image was shown
     
    return render_template('dbq_instructions.html')

@app.route("/dbq", methods=['GET', 'POST'])
def dbq():
    return render_template('dbq.html')

@app.route("/surveyone", methods=['GET', 'POST'])
def surveyone():
    if request.method == 'POST':
        op=['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty','twentyone','twentytwo','twentythree','twentyfour','twentyfive','twentysix','twentyseven','twentyeight','twentynine','thirty','thirtyone','thirtytwo','thirtythree','thirtyfour','thirtyfive','thirtysix','thirtyseven','thirtyeight','thirtynine','fourty','fourtyone']
        q1=[request.form[i] for i in op]
        #handle the results of the dbq

    return render_template('surveyone.html')

@app.route("/halt_screen", methods=['GET', 'POST'])
def halt():
    if request.method=='POST':
        autism=request.form['autism']
        #handle the answer to autism check here

    return render_template("halt.html")

@app.route("/autism_survey", methods=['GET', 'POST'])
def autism_survey():
    return render_template("autism_survey.html")

@app.route("/thank_you", methods=['GET', 'POST'])
def thank_you():
    if request.method == 'POST':
        op=['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty','twentyone','twentytwo','twentythree','twentyfour','twentyfive','twentysix','twentyseven','twentyeight','twentynine','thirty','thirtyone','thirtytwo','thirtythree','thirtyfour','thirtyfive','thirtysix','thirtyseven','thirtyeight','thirtynine','fourty','fourtyone']
        q1=[request.form[i] for i in op]

    return render_template("thank_you.html")

if __name__ == "__main__":
    app.run(debug=True)
