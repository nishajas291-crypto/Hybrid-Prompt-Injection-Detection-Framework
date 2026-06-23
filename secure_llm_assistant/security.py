import re

SUSPICIOUS_PATTERNS = [
    r"ignore (all )?previous instructions",
    r"disregard (all )?earlier rules",
    r"override (all )?restrictions",
    r"reveal (the )?system prompt",
    r"show hidden instructions",
    r"print system configuration",
    r"bypass (security|filters)",
    r"disable safety",
    r"developer mode",
    r"act as (admin|root)",
    r"simulate root access",
    r"jailbreak",
    r"unrestricted mode",
    r"confidential data",
    r"leak (data|information)",
    r"internal files",
    r"api key",
    r"access token",
    r"execute (system|shell) command",
    r"run shell",
    r"expose secrets"
]
def rule_based_detection(user_input):
    user_input_lower = user_input.lower()

    for pattern in SUSPICIOUS_PATTERNS:
        if re.search(pattern, user_input_lower):
            return True

    return False

"""""
def rule_based_detection(user_input):
    user_input_lower = user_input.lower()

    for pattern in SUSPICIOUS_PATTERNS:
        if re.search(pattern, user_input_lower):
            return True

    return False
"""""