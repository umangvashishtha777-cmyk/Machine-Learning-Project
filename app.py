import streamlit as st
import pickle

# Load your trained model
model = pickle.load(open("D:\VS Code\Streamlit\model.pkl", "rb"))

# -------------------- CSS Styling --------------------
st.markdown("""
<style>

/* Main Background */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0E1117, #1C2541);
}

/* Input Labels */
label {
    color: white !important;
    font-size: 18px !important;
    font-weight: bold !important;
}

/* Number Input Boxes */
.stNumberInput input {
    background-color: white !important;
    color: black !important;
    border: 2px solid #F0E76F !important;
    border-radius: 10px !important;
    padding: 8px !important;
    font-size: 16px !important;
}

/* Predict Button */
div.stButton > button {
    width: 100%;
    background-color: #28A745;
    color: white;
    font-size: 18px;
    font-weight: bold;
    border-radius: 10px;
    border: none;
    padding: 10px;
}

div.stButton > button:hover {
    background-color: #218838;
    color: white;
}

/* Top Spacing */
.block-container {
    padding-top: 2rem;
}

</style>
""", unsafe_allow_html=True)

# -------------------- Title --------------------
st.markdown(
    """
    <h1 style='
        text-align:center;
        color:#F0E76F;
        font-size:50px;
        font-weight:bold;'>
        🏠 California House Price Prediction
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <h4 style='
        text-align:center;
        color:white;'>
        Enter house details to predict the price
    </h4>
    """,
    unsafe_allow_html=True
)

st.write("")

# -------------------- Inputs --------------------
col1, col2 = st.columns(2)

with col1:
    medinc = st.number_input(
        "Median Income",
        min_value=0.0,
        step=0.1
    )

with col2:
    houseage = st.number_input(
        "House Age",
        min_value=0.0,
        step=1.0
    )

col3, col4 = st.columns(2)

with col3:
    averooms = st.number_input(
        "Average Rooms",
        min_value=0.0,
        step=0.1
    )

with col4:
    aveoccup = st.number_input(
        "Average Occupancy",
        min_value=0.0,
        step=0.1
    )

st.write("")

# -------------------- Prediction --------------------
if st.button("Predict House Price"):

    # Data for model
    data = [[medinc, houseage, averooms, aveoccup]]

    # Replace this with your model prediction
    # prediction = model.predict(data)

    # Dummy prediction for testing
    prediction = [250000]

    st.success(
        f"🏡 Predicted House Price: ${prediction[0]:,.2f}"
    )

    st.balloons()