
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Mercari Price Predictor",
    page_icon="🛍️",
    layout="centered"
)

@st.cache_resource
def load_model():
    return joblib.load("mercari_price_model.pkl")

model = load_model()

st.title("🛍️ Marketplace Product Price Prediction")
st.write(
    "Estimate a product's selling price using its name, "
    "category, brand, condition and shipping details."
)

with st.form("price_form"):
    name = st.text_input("Product name", "Wireless headphones")
    description = st.text_area("Product description", "Good condition")
    category = st.text_input("Product category", "Electronics/Audio")
    brand = st.text_input("Brand", "Unknown")

    condition = st.selectbox(
        "Item condition",
        [1, 2, 3, 4, 5],
        index=2
    )

    shipping = st.selectbox(
        "Who pays shipping?",
        ["Seller", "Buyer"]
    )

    submitted = st.form_submit_button("Predict price")

if submitted:
    input_data = pd.DataFrame([{
        "text_features": name + " " + description,
        "category_name": category if category.strip() else "Unknown",
        "brand_name": brand if brand.strip() else "Unknown",
        "item_condition_id": condition,
        "shipping": 1 if shipping == "Seller" else 0
    }])

    prediction = max(0, float(model.predict(input_data)[0]))

    st.success(f"Estimated product price: ${prediction:.2f}")
    st.caption(
        "This is a model estimate, not a guaranteed selling price."
    )
