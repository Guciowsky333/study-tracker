import json
import time
from datetime import datetime, timedelta, date
import requests
from dotenv import load_dotenv
import os


load_dotenv()
webhook_url = os.getenv('DC_WEBHOOK_URL')


def format_time(time_in_seconds:int) -> str:
    parts = []
    hours = time_in_seconds // 3600
    minutes = (time_in_seconds % 3600) // 60
    seconds = time_in_seconds % 60

    if hours > 0:
        parts.append(f"{hours}h")
    if minutes > 0:
        parts.append(f"{minutes}m")
    if seconds > 0:
        parts.append(f"{seconds}s")

    return " ".join(parts)

def calculate_streak(last_date:str, streak:int) -> int:
    now = date.today()
    last_date = datetime.strptime(last_date, "%Y-%m-%d").date()


    if last_date == now - timedelta(days=1):
        return streak + 1

    if last_date == now:
        return streak
    return 1

def send_message(webhook:str, message:str) -> None:
    body = {
        "content": message,
    }
    response = requests.post(webhook, data=body)
    if response.status_code != 204:
        print("Failed to send message!")



if __name__ == "__main__":
    today = date.today()
    with open("date.json") as f:
        data = json.load(f)

    start_time = time.perf_counter()

    input("Press ENTER to stop:")
    end_time = time.perf_counter()


    session = end_time - start_time


    current_streak = calculate_streak(data["last_date"], data["streak"])




    new_data ={
        "last_date": today.strftime("%Y-%m-%d"),
        "streak": current_streak,
        "total_time": data["total_time"] + session,
    }

    message_to_send = (f"Today's you studied for {format_time(int(session))} \n"
                       f"Your current streak is {current_streak} \n"
                       f"And you overall time of learning is {format_time(int(new_data['total_time']))} \n"
                       f"-----------------------------------")
    send_message(webhook_url, message_to_send)

    with open("date.json", "w") as f:
        json.dump(new_data, f)









