import openai
import os
from dotenv import load_dotenv

class GPTResponseGenerator:
    def __init__(self):
        # Load settings from .env file
        load_dotenv()
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.model = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
        self.max_tokens = int(os.getenv("MAX_TOKENS", 150))
        self.temperature = float(os.getenv("TEMPERATURE", 0.5))
        # Initialize the OpenAI client with the API key
        self.client = openai.OpenAI(api_key=self.api_key)

    def generate_response(self, system_message, user_message):
        print("\nResponse Generator User Message:", user_message)
        print("Response Generator System Message:", system_message)
        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message}
        ]

        response = self.client.chat.completions.create(
            messages=messages,
            model=self.model,
            max_tokens=self.max_tokens,
            temperature=self.temperature
        )
        
        return response.choices[0].message.content

# Usage Example:
# gpt_generator = GPTResponseGenerator()
# response = gpt_generator.generate_response("System message here", "User message here")
# print(response)
