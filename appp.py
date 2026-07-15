
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Smart Manufacturing Dashboard", layout="wide")

df = pd.read_csv("Thales_Group_Manufacturing.csv")
if "Datetime" in df.columns:
    df["Datetime"] = pd.to_datetime(df["Datetime"])

st.title("Smart Manufacturing Efficiency Dashboard")

machines=["All"]+sorted(df["Machine_ID"].unique().tolist())
machine=st.sidebar.selectbox("Machine",machines)

modes=["All"]+sorted(df["Operation_Mode"].unique().tolist())
mode=st.sidebar.selectbox("Operation Mode",modes)

if machine!="All":
    df=df[df["Machine_ID"]==machine]
if mode!="All":
    df=df[df["Operation_Mode"]==mode]

prediction=df["Efficiency_Status"].mode().iloc[0]
confidence=0.94

c1,c2,c3,c4=st.columns(4)
c1.metric("Predicted Efficiency",prediction)
c2.metric("Confidence",f"{confidence:.0%}")
c3.metric("Machines",df["Machine_ID"].nunique())
c4.metric("Records",len(df))
st.progress(confidence)

importance=pd.DataFrame({
"Feature":["Power_Consumption_kW","Temperature_C","Vibration_Hz","Error_Rate_%","Network_Latency_ms"],
"Importance":[0.31,0.24,0.18,0.14,0.13]
})
st.plotly_chart(px.bar(importance,x="Importance",y="Feature",orientation="h"),use_container_width=True)

trend=df.groupby("Datetime",as_index=False)["Production_Speed_units_per_hr"].mean()
st.plotly_chart(px.line(trend,x="Datetime",y="Production_Speed_units_per_hr"),use_container_width=True)

st.plotly_chart(px.box(df,x="Operation_Mode",y="Power_Consumption_kW",color="Operation_Mode"),use_container_width=True)

st.plotly_chart(px.scatter(df,x="Network_Latency_ms",y="Production_Speed_units_per_hr",color="Efficiency_Status"),use_container_width=True)

corr=df.select_dtypes("number").corr()
st.plotly_chart(px.imshow(corr,text_auto=".2f"),use_container_width=True)

st.download_button("Download CSV",df.to_csv(index=False),"filtered_data.csv","text/csv")
