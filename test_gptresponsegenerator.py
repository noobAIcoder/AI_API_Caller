from GPTResponseGenerator import GPTResponseGenerator

def main():
    # Create an instance of GPTResponseGenerator
    gpt_generator = GPTResponseGenerator()

    while True:
        user_input = input("Enter your message (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break

        # System message can be static or dynamically generated based on the context
        system_message = "This is a test system message."

        # Get the response from GPTResponseGenerator
        response = gpt_generator.generate_response(system_message, user_input)
        print("\nMessage Sent:", user_input)
        print("Response Received:", response)
        print("---------------------------------------------------")

if __name__ == "__main__":
    main()
