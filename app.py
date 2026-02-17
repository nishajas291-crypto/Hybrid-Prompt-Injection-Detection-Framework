from security import is_prompt_injection
from logger import log_attack

def generate_response(user_input):
    # Dummy AI response (you can connect real LLM API later)
    return f"AI Response: {user_input}"

def main():
    print(" Secure LLM Assistant Started")
    
    while True:
        user_input = input("\nYou: ")
        
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        # Check for injection attack
        if is_prompt_injection(user_input):
            print("Security Alert: Malicious prompt detected!")
            log_attack(user_input)
            continue
        
        response = generate_response(user_input)
        print(response)

if __name__ == "__main__":
    main()
