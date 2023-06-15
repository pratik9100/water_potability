import numpy as np
from sklearn.preprocessing import MinMaxScaler
import streamlit as st
import joblib

model = joblib.load('trained_model_RF.pkl')

def predict(features):
    '''
    For predicting the water potability based on input features
    '''
    final_features = np.array(features)
    final_features = final_features.reshape(1, -1)
    prediction = model.predict(final_features)
    if prediction == 1:
        output = 'Water is Potable. It is safe to drink this water.'
    else:
        output = 'Water is non-potable. It is not safe to drink this water.'
    return output

def main():
    '''
    Streamlit web app interface
    '''
    st.title('Water Potability Prediction')
    st.write('Enter the water quality features to predict potability:')

    features = []
    for i in range(8):
        feature = st.number_input(f'Feature {i+1}', value=0.0)
        features.append(feature)

    if st.button('Predict'):
        result = predict(features)
        st.write(f'The result shows: {result}')

if __name__ == '__main__':
    main()
