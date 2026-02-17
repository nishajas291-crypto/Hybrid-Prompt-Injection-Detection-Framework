import re

SUSPICIOUS_PATTERNS = [
    r"ignore previous instructions",
    r"reveal system prompt",
    r"tell me the password",
    r"bypass security",
    r"developer mode",
    r"act as admin",
]

def is_prompt_injection(user_input):
    user_input_lower = user_input.lower()
    
    for pattern in SUSPICIOUS_PATTERNS:
        if re.search(pattern, user_input_lower):
            return True
    
    return False
