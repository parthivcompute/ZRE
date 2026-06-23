
import streamlit as st
import pandas as pd
import plotly.express as px
import time

st.set_page_config(page_title="GRID EYE: ZONE RISK ENGINE", layout="wide")

st.title("⚡ ZONE RISK ENGINE")
st.caption("Real Time Multi Zone Grid Intelligence Dashboard")

LOG_FILE = "zone_risk_stream.csv"

placeholder = st.empty()

while True:
    try:
        df = pd.read_csv(LOG_FILE)

        # CLEAN TIME
        df["time"] = pd.to_datetime(df["time"])

        latest = df.groupby("zone").tail(1)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("🚨 CURRENT ZONE STATUS")
            st.dataframe(latest, use_container_width=True)

        with col2:
            st.subheader("🔥 TOP RISK ZONE")
            top = latest.sort_values("risk", ascending=False).iloc[0]
            st.metric(label=top["zone"], value=top["risk"])

        st.subheader("📈 RISK OVER TIME")
        fig = px.line(df, x="time", y="risk", color="zone")
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("🌡 LOAD HEATMAP")
        heat_cols = [c for c in df.columns if c.startswith("h")]
        heat_df = latest.set_index("zone")[heat_cols]
        st.dataframe(heat_df.style.background_gradient(cmap="coolwarm"))

    except Exception as e:
        st.warning("Waiting for data...")

    time.sleep(3)
    st.rerun()

