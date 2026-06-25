import json
import time



def format_time(time_in_seconds) -> str:
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










