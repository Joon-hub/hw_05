import pickle

# Load the DictVectorizer
with open('dv.bin', 'rb') as f_dv:
    dv = pickle.load(f_dv)

# Load the LogisticRegression model
with open('model1.bin', 'rb') as f_model:
    model = pickle.load(f_model)

# Client data
client = {"job": "management", "duration": 400, "poutcome": "success"}

# Transform the client data
X = dv.transform([client])

# Predict the probability
probability = model.predict_proba(X)[0, 1]

print(f"The probability that this client will get a subscription is: {probability:.4f}")