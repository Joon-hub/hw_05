import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the DictVectorizer
with open('dv.bin', 'rb') as f_dv:
    dv = pickle.load(f_dv)

# Load the LogisticRegression model
with open('model1.bin', 'rb') as f_model:
    model = pickle.load(f_model)
@app.route('/',methods=['GET'])
def hello():
    return "Hello, World!"
@app.route('/predict', methods=['POST'])
def predict():
    client = request.get_json()
    X = dv.transform([client])
    y_pred = model.predict_proba(X)[0, 1]
    return jsonify({'probability': float(y_pred)})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)

# check the code is running 
# curl -X POST -H "Content-Type: application/json" -d '{"job": "management", "duration": 400, "poutcome": "success"}' http://localhost:9696/predict