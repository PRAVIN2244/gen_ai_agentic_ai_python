import asyncio
import streamlit as st

from app import get_weather


st.set_page_config(
    page_title="Weather App",
    page_icon="🌤️"
)

st.title("🌤️ Weather Information")

city = st.text_input(
    "Enter City",
    placeholder="Example: Hyderabad"
)


if st.button("Get Weather"):

    if not city.strip():

        st.warning("Please enter a city")

    else:

        with st.spinner("Getting weather information..."):

            try:

                weather = asyncio.run(
                    get_weather(city)
                )

                st.success(f"Weather in {city}")

                col1, col2 = st.columns(2)

                with col1:
                    st.metric(
                        "Temperature",
                        weather["temperature"]
                    )

                with col2:
                    st.metric(
                        "Condition",
                        weather["condition"]
                    )

            except Exception as e:

                st.error(
                    f"Unable to get weather information: {e}"
                )