from datetime import datetime

def log_attack(user_input):
    with open("attack_log.txt", "a") as file:
        file.write(f"[{datetime.now()}] Suspicious Prompt: {user_input}\n")
