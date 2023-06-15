import streamlit as st

def main():
    st.title("Water Potability Prediction")
    st.write("Please enter the following details")

    ph = st.number_input("ph", step=0.01)
    hardness = st.number_input("Hardness", step="any")
    solids = st.number_input("Solids")
    chloramines = st.number_input("Chloramines", step=0.01)
    sulfate = st.number_input("Sulfate")
    conductivity = st.number_input("Conductivity")
    organic_carbon = st.number_input("Organic_carbon", step=0.01)
    trihalomethanes = st.number_input("Trihalomethanes")
    turbidity = st.number_input("Turbidity", step=0.01)

    if st.button("Predict"):
        # Perform prediction based on the input values
        prediction = predict_potability(ph, hardness, solids, chloramines, sulfate, conductivity,
                                       organic_carbon, trihalomethanes, turbidity)

        if prediction == 1:
            output = 'Water is Potable. It is safe to drink this water.'
        else:
            output = 'Water is non-potable. It is not safe to drink this water.'

        st.write("The Result shows: " + output)

def predict_potability(ph, hardness, solids, chloramines, sulfate, conductivity,
                       organic_carbon, trihalomethanes, turbidity):
    # Use the loaded model to perform prediction
    # Replace this with your actual prediction code
    prediction = 1
    return prediction

if __name__ == "__main__":
    main()
