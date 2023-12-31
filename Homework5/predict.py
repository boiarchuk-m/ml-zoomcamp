import pickle
from flask import Flask

from flask import request
from flask import jsonify

with open('model1.bin', 'rb') as f_in: 
    model = pickle.load(f_in)

with open('dv.bin', 'rb')as f_in:
    dict_vectorizer = pickle.load(f_in)
     

customer = {"job": "retired", "duration": 445, "poutcome": "success"}

app = Flask('churn')

@app.route('/predict', methods = ['POST'])
def predict():

    customer  = request.get_json()
    X =dict_vectorizer.transform(customer)
    y_pred = model.predict_proba(X)[0,1]
    churn = y_pred>=0.5

    result = {'probability': float(y_pred),
              'churn': bool(churn)}
    return jsonify(result)


if __name__ =="__main__":
    app.run(debug=True, host = '0.0.0.0', port=9696)
