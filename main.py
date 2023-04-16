import streamlit as st
import plotly.express as px

st.title("Weather Forecast fot the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of Forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")


def get_data(days):
    dates = ["2023-25-04", "2023-26-04", "2023-27-04"]
    temperatures = [10, 11, 13]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures


d, t = get_data(days)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperatures (C)"})
st.plotly_chart(figure)