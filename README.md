AI API Caller
Overview

The AI API Caller repository is a collection of Python scripts designed to simplify interacting with various AI APIs. The current focus is on OpenAI's GPT models, providing an easy and efficient way for users to send queries and receive responses from the GPT-3.5 API.
Contents

This repository includes:

    GPTResponseGenerator.py: A script that encapsulates the functionality for sending requests to and receiving responses from the OpenAI GPT-3.5 API.
    test_gptresponsegenerator.py: A demonstration script showing how to use GPTResponseGenerator.py to send messages to the API and display responses.
    README.md: Documentation explaining the purpose and usage of the scripts within the repository.

Prerequisites

    Python 3.x
    OpenAI API Key

Setup and Installation

    Clone the Repository:

    bash

git clone https://github.com/noobAIcoder/AI_API_Caller.git

Install Dependencies:

    Run pip install openai python-dotenv to install the necessary Python packages.

API Key Configuration:

    Create a .env file in the root directory.
    Add your OpenAI API key:

    arduino

        OPENAI_API_KEY='your_api_key_here'

Usage

    To utilize the GPTResponseGenerator, import it into your Python project and instantiate it.
    Use the test_gptresponsegenerator.py script to see a demonstration of sending a user message to the OpenAI GPT API and receiving a response.

Customization

You can modify the scripts to suit your specific needs, such as changing API parameters or handling different AI models.
Contributions

Contributions, suggestions, and feedback are welcome. Please ensure to follow the project's code style and guidelines.
License

This project is licensed under the MIT License.