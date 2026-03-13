from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open("model/disease_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    fever = int(request.form["fever"])
    cough = int(request.form["cough"])
    headache = int(request.form["headache"])
    fatigue = int(request.form["fatigue"])

    prediction = model.predict([[fever, cough, headache, fatigue]])

    return render_template("result.html", result=prediction[0])

if __name__ == "__main__":
    app.run(debug=True)