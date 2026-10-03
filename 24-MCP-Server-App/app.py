from fastmcp import FastMCP
from weather_service import weather_data
import os
from dotenv import load_dotenv
from slack_sdk import WebClient

load_dotenv()

# Connect to slack
slack = WebClient(
    token = os.getenv("SLACK_BOT_TOKEN")
)

# Create MCP Server
mcp = FastMCP("Weather Server")



@mcp.tool
def get_weather(city:str):
    """
    Return Weather information of given city
    """
    return weather_data.get(city, "No Data Found")

@mcp.tool
def send_message(message:str):
    """ Send a message to slack """
    slack.chat_postMessage(
        channel = os.getenv("SLACK_CHANNEL"),
        text = message
    )

    return "Message Sent Successfully"


@mcp.tool
def read_messages(limit: int = 10):
    """Read recent messages from Slack channel"""

    response = slack.conversations_history(
        channel=os.getenv("SLACK_CHANNEL"),
        limit=limit
    )

    messages = response.get("messages", [])

    if not messages:
        return "No messages found."

    result = []

    for msg in messages:
        user = msg.get("user", "Unknown User")
        text = msg.get("text", "")

        result.append(f"{user}: {text}")

    return "\n".join(result)

if __name__ == "__main__":
    mcp.run(
        transport = "http",
        host = "localhost",
        port = 8081
    )