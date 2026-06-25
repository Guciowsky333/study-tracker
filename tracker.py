import json
import time
from datetime import datetime, timedelta, date
from dotenv import load_dotenv
load_dotenv()
import requests



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

    with open("date.json", "w") as f:
        json.dump(new_data, f)









