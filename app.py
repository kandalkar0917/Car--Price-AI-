import streamlit as st
import pandas as pd

st.set_page_config(page_title="Car Price AI", page_icon="🚗")

st.markdown("""
<style>
.big-box {background: linear-gradient(90deg, #667eea, #764ba2); padding: 20px; border-radius: 15px; color: white; text-align: center;}
.price-box {background: #f0f2f6; padding: 20px; border-radius: 15px; text-align: center; border: 2px solid #667eea;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="big-box"><h1>🚗 CAR PRICE AI</h1><p>Second Hand Car ki Sahi Kimat - 1 Minute Me</p></div>', unsafe_allow_html=True)
st.write("")

col1, col2 = st.columns(2)
with col1:
    brand = st.selectbox("🚙 Brand Chuno", ["Maruti", "Hyundai", "Honda", "Tata"])
with col2:
    model = st.selectbox("✨ Model Chuno", ["Swift", "Creta", "City", "Nexon"])

col3, col4, col5 = st.columns(3)
with col3:
    year = st.slider("📅 Year", 2015, 2024, 2020)
with col4:
    km = st.slider("🛣️ KM Chali?", 5000, 150000, 40000)
with col5:
    condition = st.slider("⭐ Condition 1-10", 1, 10, 8)

fuel = st.radio("⛽ Fuel Kya Hai?", ["Petrol", "Diesel", "CNG"], horizontal=True)

if st.button("🔮 AI Se Price Pata Karo", use_container_width=True):
    age = 2026 - year
    base = {"Maruti": 550000, "Hyundai": 650000, "Honda": 800000, "Tata": 600000}[brand]
    price = base - (age*40000) - (km*1.2) + (condition*15000)
    price = int(price)
    low = int(price*0.92)
    high = int(price*1.08)

    st.markdown(f'<div class="price-box"><h2>💰 Fair Price: ₹ {price:,}</h2><p>Range: ₹ {low:,} - ₹ {high:,}</p></div>', unsafe_allow_html=True)
    st.write("")

    if km < 30000 and condition >= 8:
        st.success("🔥 SUPER DEAL HAI! Jaldi Kharid Lo")
        st.balloons()
    elif km < 60000:
        st.info("👍 GOOD DEAL HAI - Price Bilkul Sahi Hai")
    else:
        st.warning("⚠️ SOCH KE LO - Car Zyada Chali Hui Hai")

    c1, c2, c3 = st.columns(3)
    c1.metric("👤 Buyer Ke Liye", f"₹ {high:,}", "Isse zyada mat dena")
    c2.metric("🏷️ Seller Ke Liye", f"₹ {price:,}", "Ispe rakho, jaldi bikegi")
    c3.metric("🏪 Dealer Profit", f"₹ {high-low:,}", "Itna profit hoga")

    st.write("### 📊 Price Pe Kiska Kitna Asar?")
    chart_data = pd.DataFrame({
        "Factor": ["Age", "KM", "Condition", "Brand"],
        "Effect": [-age*8, -km//1000, condition*5, 20]
    })
    st.bar_chart(chart_data.set_index("Factor"))

    st.write("### 👀 Market Me Aisi Hi 3 Cars")
    st.write(f"1. {brand} {model} {year-1} - {km+5000} KM - ₹ {price+20000:,}")
    st.write(f"2. {brand} {model} {year} - {km-3000} KM - ₹ {price-15000:,}")
    st.write(f"3. {brand} {model} {year+1} - {km+10000} KM - ₹ {price+40000:,}")
else:
    st.info("👆 Upar se Car Chuno aur Button Dabao - Jadu Dekho!")

st.caption("Made By AI-Based Used Vehicle Price Intelligence System | MBA Project")
