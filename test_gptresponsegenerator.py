from GPTResponseGenerator import GPTResponseGenerator
import os
from dotenv import load_dotenv

def main():
    # Load environment variables
    load_dotenv()

    # Retrieve the system message from .env
    system_message = os.getenv("WHOAREYOU_SYSTEM_MESSAGE", "Default system message")

    # Create an instance of GPTResponseGenerator
    gpt_generator = GPTResponseGenerator()

    while True:
        user_input = input("Enter your message (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break

        # Get the response from GPTResponseGenerator
        user_message = user_input
        response = gpt_generator.generate_response(system_message, user_message)
        print("\nTest Unit User Message:", user_message)
        print("Test Unit System Message:", system_message)
        print("Test Unit Response Received:", response)
        print("---------------------------------------------------")

if __name__ == "__main__":
    main()
