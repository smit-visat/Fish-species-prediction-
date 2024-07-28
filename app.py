from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load the trained model and scaler
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    final_features = np.array(features).reshape(1, -1)
    final_features_scaled = scaler.transform(final_features)
    prediction = model.predict(final_features_scaled)
    return render_template('index.html', prediction_text=f'The predicted species is {prediction[0]}')

if __name__ == "__main__":
    app.run(debug=True)
