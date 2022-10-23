from flask import Flask,request, render_template
import joblib
import numpy as np

app = Flask(__name__)

model=joblib.load('model.joblib')


@app.route('/')
def homepage():
    return render_template("index.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    gender = int(request.form.get("Gender"))
    age = int(request.form.get("Age"))
    cs = int(request.form.get("Credit Score"))
    tenure = int(request.form.get("Tenure"))
    bankbal = int(request.form.get("Bank Balance"))
    numofprods = int(request.form.get("Number of Products"))
    sal = int(request.form.get("Salary"))
    place = request.form.get("Place")
    creditcard = int(request.form.get("Has Credit Card?"))
    activemember = int(request.form.get("Is Active Member?"))

    x, y, z = 0, 0, 0

    if place == 'MUB':
        x = 1
        y = 0
        z = 0
    elif place == 'DEL':
        x = 0
        y = 1
        z = 0
    else:
        x = 0
        y = 0
        z = 1

    a = list([  cs,age, tenure, bankbal, numofprods, creditcard, activemember,sal, x, y, z, gender])
    final = [np.array(a)]
    model = joblib.load('model.joblib')
    adi = model.predict(final)
    if adi == [0]:
      data = "Will stay"
    else:
      data = 'Will exit'
    return render_template("final.html", data = data)



if __name__ == '__main__':
    app.run(debug=True)