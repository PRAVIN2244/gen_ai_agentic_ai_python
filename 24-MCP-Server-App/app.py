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
    slack.chat_postMesage(
        channel = os.getenv("SLACK_CHANNEL"),
        text = message
    )

    return "Message Sent Successfully"




if __name__ == "__main__":
    mcp.run(
        transport = "http",
        host = "localhost",
        port = 8081
    )