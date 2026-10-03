import streamlit as st
import asyncio

from app import (
    get_weather,
    send_slack_message,
    read_slack_messages
)


st.set_page_config(
    page_title="MCP Client",
    page_icon="🤖",
    layout="wide"
)


st.title("🤖 MCP Client")
st.caption("Streamlit → FastMCP Client → MCP Server → Slack")


# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.header("MCP Tools")

    option = st.radio(
        "Select Operation",
        [
            "🌤️ Get Weather",
            "📤 Send Slack Message",
            "📥 Read Slack Messages"
        ]
    )


# =====================================================
# WEATHER
# =====================================================

if option == "🌤️ Get Weather":

    st.header("🌤️ Get Weather")

    city = st.text_input(
        "Enter City",
        placeholder="Hyderabad"
    )

    if st.button(
        "Get Weather",
        type="primary"
    ):

        if not city:

            st.warning("Please enter a city.")

        else:

            try:

                with st.spinner("Calling MCP Server..."):

                    result = asyncio.run(
                        get_weather(city)
                    )

                st.success("Weather received")

                st.write(result)

            except Exception as e:

                st.error(str(e))


# =====================================================
# SEND SLACK MESSAGE
# =====================================================

elif option == "📤 Send Slack Message":

    st.header("📤 Send Slack Message")

    message = st.text_area(
        "Message",
        placeholder="Enter message to send to Slack...",
        height=150
    )

    if st.button(
        "Send Message",
        type="primary"
    ):

        if not message.strip():

            st.warning("Please enter a message.")

        else:

            try:

                with st.spinner("Sending message..."):

                    result = asyncio.run(
                        send_slack_message(message)
                    )

                st.success(result)

            except Exception as e:

                st.error(str(e))


# =====================================================
# READ SLACK MESSAGES
# =====================================================

elif option == "📥 Read Slack Messages":

    st.header("📥 Read Slack Messages")

    limit = st.number_input(
        "Number of messages",
        min_value=1,
        max_value=100,
        value=10
    )

    if st.button(
        "Read Messages",
        type="primary"
    ):

        try:

            with st.spinner("Reading Slack messages..."):

                result = asyncio.run(
                    read_slack_messages(limit)
                )

            st.success("Messages received")

            st.text_area(
                "Slack Messages",
                value=result,
                height=400
            )

        except Exception as e:

            st.error(str(e))