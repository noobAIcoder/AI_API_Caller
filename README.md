# AI API Caller

## Overview
The AI API Caller is a suite of Python scripts designed to interface with OpenAI's GPT-3.5 model. This project simplifies sending queries to the API and managing the responses, allowing for easy integration into various applications. It includes scripts for direct API interaction and for processing data from Excel files.

## Files in the Repository
- `GPTResponseGenerator.py`: The core class for interacting with the OpenAI GPT API.
- `test_gptresponsegenerator.py`: A tst script to test the GPTResponseGenerator by sending user-input messages.
- `test_xlsx2db_gptresponsegenerator.py`: A script that reads questions from an Excel file, queries the OpenAI API, and stores responses in both a new Excel file and a SQLite database.
- `.env.example`: An example of the environment file for setting up necessary configurations.

## Prerequisites
- Python 3.x
- OpenAI API Key
- Python packages: `openai`, `openpyxl`, `python-dotenv`, `sqlite3` (usually included in standard Python installations)

## Setup
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/AI_API_Caller.git
   ```
2. **Install Required Python Packages:**
   ```bash
   pip install openai openpyxl python-dotenv
   ```
3. **Set Up the .env File:**
   - Rename `.env.example` to `.env`.
   - Fill in the necessary details like your OpenAI API key.

## Usage

### GPTResponseGenerator
This script is used to interact with the OpenAI GPT API.

#### Example Usage:
```python
from GPTResponseGenerator import GPTResponseGenerator

gpt_generator = GPTResponseGenerator()
response = gpt_generator.generate_response("System message here", "User message here")
print(response)
```

### Test GPTResponseGenerator
Use this script to manually send messages to the API and see the responses.

#### Running the Test Script:
```bash
python test_gptresponsegenerator.py
```

### Test XLSX to DB GPTResponseGenerator
This script reads data from an Excel file, sends it to the OpenAI API, and stores the responses in a new Excel file and a SQLite database.

#### Preparing Your Excel File:
- Ensure your Excel file has questions in the first three columns.
- Name the file as per the path specified in your `.env` file.

#### Running the Script:
```bash
python test_xlsx2db_gptresponsegenerator.py
```

## Contributions
Contributions, suggestions, and feedback are welcome. Please adhere to the project's code style and guidelines when making contributions.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
