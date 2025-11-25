
from dotenv import load_dotenv
import json
import os
import requests

load_dotenv()


SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")


def send_slack_notification(date, summary):
    text = f":information_source: *Techonology News for {date}*: ```\n{summary}\n``` "
    payload = {
        "username": "NotificationBot",
        "icon_emoji": ":robot_face:",
        "blocks":  [{
            "type": "section",
            "text": {
                    "type": "mrkdwn",
                    "text": text,
            },
        },]
    }
    response = requests.post(SLACK_WEBHOOK_URL, data=json.dumps(payload))
