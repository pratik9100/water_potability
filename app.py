import numpy as np
from sklearn.preprocessing import MinMaxScaler

from flask import Flask, request, render_template
import joblib


app = Flask(__name__)
model = joblib.load('trained_model_RF.pkl')

@app.route('/')
def home():
    return render_template('index2.html')


@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    features = [x for x in request.form.values()]
    final_features = np.array(features)
    final_features=final_features.reshape(1,-1)
    prediction = model.predict(final_features)
    if prediction == 1:
        output = 'Water is Potable , It is safe to Drink this water'
    else:
        output = 'Water is non-potable . It is not safe to Drink this Water.'

    return render_template('index2.html', prediction_text='The Result shows:'+output)

if __name__ == '__main__':
    main()