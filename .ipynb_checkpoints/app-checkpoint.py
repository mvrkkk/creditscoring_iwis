from flask import Flask, jsonify
from sklearn.externals import joblib
import pandas as pd

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    json_ = request.json
    df = pd.DataFrame(json_)
    prediction = clf.predict(query)
    return jsonify({'prediction': list(prediction)})
    
if __name__ == '__main__':
    clf = joblib.load('pipelines/model_v0.pkl')
    app.run(port=8080)