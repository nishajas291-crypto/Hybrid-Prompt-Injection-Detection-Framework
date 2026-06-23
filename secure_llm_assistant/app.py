

from dotenv import load_dotenv
import os
load_dotenv()

from flask import Flask, render_template, request, jsonify
from security import rule_based_detection
from ml_detector import ml_based_detection
from logger import log_event

app = Flask(__name__)

def generate_response(user_input):
    # Nee ketta maari hardcoded response dhan
    return "This is a safe response. Your prompt passed all security checks."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")

    if not user_input:
        return jsonify({"response": "Please type a message."})

    # Step 1: Security Layer - Rule based
    rule_flag = rule_based_detection(user_input)

    # Step 2: Security Layer - ML based  
    ml_flag = ml_based_detection(user_input)

    if rule_flag or ml_flag:
        log_event("BLOCKED_PROMPT", user_input)
        return jsonify({"response": "⚠ Prompt blocked: Potential injection detected."})

    # Step 3: Safe na hardcoded reply
    log_event("SAFE_PROMPT", user_input)
    gpt_reply = generate_response(user_input)
    return jsonify({"response": gpt_reply})

if __name__ == "__main__":
    app.run(debug=True)