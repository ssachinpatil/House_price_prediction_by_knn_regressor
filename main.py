
from utils import house
from flask import Flask,jsonify,request,render_template
import numpy as np

app=Flask(__name__)
@app.route('/')
def home():
     return render_template("sms.html")

@app.route('/result',methods=["POST"])
def result():
    i=request.form.get
    X1transactiondate=float(i("X1transactiondate"))
    X2houseage=float(i('X2houseage'))
    X3distancetothenearestMRTstation=float(i("X3distancetothenearestMRTstation"))
    X4numberofconveniencestores=float(i('X4numberofconveniencestores'))
    X5latitude=float(i("X5latitude"))
    X6longitude=float(i("X6longitude"))

    ans=house(X1transactiondate,X2houseage,X3distancetothenearestMRTstation,X4numberofconveniencestores,X5latitude,X6longitude)
    res=ans.pred1()

    return render_template("sms.html",pred=res)
    # return jsonify({'answer':f'The house price per unit area is {res} $ only'})
if __name__=="__main__":
    app.run(port=3000)