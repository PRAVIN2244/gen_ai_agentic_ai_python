import os

from dotenv import load_dotenv
from slack_sdk import WebClient


load_dotenv()

token = os.getenv("SLACK_BOT_TOKEN")
channel = os.getenv("SLACK_CHANNEL_ID")

slack = WebClient(token=token)


response = slack.chat_postMessage(
    channel=channel,
    text="Hello from Python!"
)

print(response)