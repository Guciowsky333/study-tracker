import json
import time
from datetime import datetime, timedelta, date



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
        streak += 1
    else:
        streak = 1
    return streak


=




