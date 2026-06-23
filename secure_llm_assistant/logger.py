from datetime import datetime

def log_event(event_type, user_input):
    with open("security_logs.txt", "a", encoding="utf-8") as file:
        file.write(f"[{datetime.now()}] {event_type}: {user_input}\n")
