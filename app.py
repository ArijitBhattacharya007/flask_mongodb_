from flask import Flask,request,render_template
from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017")
db=client["student"]
collection=db["registration"]


app = Flask(__name__)


@app.route('/',methods=["GET","POST"])
def index():  # put application's code here
    return render_template("index.html")

@app.route("/submit",methods=["GET","POST"])
def submit():
    name=request.form["name"]
    registration_number=request.form["registration_number"]
    roll_number=request.form["roll_number"]
    email=request.form["email"]
    school=request.form["school"]
    phone=request.form["phone"]
    admission_year=request.form["admission_year"]
    address=request.form["address"]
    collection.insert_one({"name":name,"registration_number":registration_number,"roll_number":roll_number,"email":email,"school":school,"phone":phone,"admission_year":admission_year,"address":address})
    data=collection.find()
    return render_template("dashboard.html",data=data)


if __name__ == '__main__':
    app.run()
