import streamlit as st
import pandas as pd
import pickle

# Load model
with open("best_ad_revenue_model.pkl", "rb") as f:
    model = pickle.load(f)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #f9f9f9;
    }

    .title-container {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 12px;
        white-space: nowrap;
    }

    .title-container h1 {
        font-size: 32px;
        margin: 0;
        white-space: nowrap;
    }
    </style>

    <div class="title-container">
        <img src="data:image/png;base64,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"
             width="50">
        <h1>YouTube Ad Monetization Modeler</h1>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    div[data-baseweb="input"] > div {
        background-color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Inputs
views = st.number_input("Views", 0)
likes = st.number_input("Likes", 0)
comments = st.number_input("Comments", 0)
watch_time = st.number_input("Watch Time (minutes)", 0.0)
video_length = st.number_input("Video Length (minutes)", 0.0)
subscribers = st.number_input("Subscribers", 0)
category = st.selectbox("Category", ['Education','Entertainment','Gaming','Lifestyle','Music','Tech'])
device = st.selectbox("Device", ['Mobile','Desktop','TV','Tablet'])
country = st.selectbox("Country", ['US','UK','IN','DE','CA'])
year = st.selectbox("Year", [2024, 2025])
engagement_rate = (likes + comments) / max(views, 1)
month = st.selectbox("Month", list(range(1, 13)))
dates = st.selectbox("Dates", list(range(1,32 )))
days = st.selectbox("Days --> ' Monday=0, Sunday=6' ", list(range(0,7 )))
weekend = st.selectbox("Weekend?  --> '1 for weekend, 0 for weekday'", [0, 1])



input_df = pd.DataFrame([{
    'views': views,
    'likes': likes,
    'comments': comments,
    'watch_time_minutes': watch_time,
    'video_length_minutes': video_length,
    'subscribers': subscribers,
    'year': year,
    'engagement_rate': engagement_rate,
    'month': month,
    'weekend': weekend,
    'category': category,
    'device': device,
    'dates': dates,
    'days': days,
    'country': country
}])

if st.button("Predict Ad Revenue"):
    revenue = model.predict(input_df)[0]
    st.success(f"💰 Predicted Ad Revenue: ${revenue:.2f}")

    if weekend == 1:
        st.info("📌 Recommendation: Posting on **weekends** increases revenue.")
    else:
        st.info("📌 Recommendation: Try posting on **weekends** for higher revenue.")




