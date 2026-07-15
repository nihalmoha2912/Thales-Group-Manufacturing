import streamlit as st
st.sidebar.selectbox(
    "Machine",
    df["Machine_ID"].unique()
)

st.sidebar.selectbox(
    "Operation Mode",
    df["Operation_Mode"].unique()
)

st.sidebar.date_input(
    "Date Range"
)

st.sidebar.slider(
    "Confidence Threshold",
    0.0,
    1.0,
    0.8
)
st.metric(
    "Predicted Efficiency",
    prediction
)

st.progress(confidence)

st.write(
    f"Confidence: {confidence:.2%}"
)
fig = px.bar(
    importance.head(10),
    x="Importance",
    y="Feature"
)

st.plotly_chart(fig)
trend = df.groupby(
    ['Datetime','Machine_ID']
)['Production_Output_Units'].mean().reset_index()

fig = px.line(
    trend,
    x='Datetime',
    y='Production_Output_Units',
    color='Machine_ID'
)

st.plotly_chart(fig)
fig = px.box(
    df,
    x='Operation_Mode',
    y='Power_Consumption_kW',
    color='Operation_Mode'
)

st.plotly_chart(fig)
fig = px.scatter(
    df,
    x='Network_Latency_ms',
    y='Production_Output_Units',
    color='Efficiency_Status'
)

st.plotly_chart(fig)