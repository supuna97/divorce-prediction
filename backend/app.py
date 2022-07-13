from flask import Flask
from flask import request

import pickle

app = Flask(__name__)


@app.route("/api/v1/divorce/predict", methods=['POST'])
def hello_world():
    content = request.json
    print(content)

    model = pickle.load(open('knn', 'rb'))
    print("Model: {}", model)
    ll = ['23', '32', '34', '65', '23', '7', '88', '65']
    ll3 = []
    print("ll3: {}", ll3)
    ll3.append(ll)
    scaler = pickle.load(open('MNScaller', 'rb'))
    print("scaler: {}", scaler)
    ll2 = scaler.transform(ll3)
    print("ll2: {}", ll2)
    prediction = model.predict(ll2)
    print("prediction: {}", prediction)
    predictionResult = int(prediction[0])
    hasDevorce = predictionResult > 0
    return {
        "Has Devorce? ": hasDevorce
    }


if __name__ == "__main__":
    app.run(debug=True)
