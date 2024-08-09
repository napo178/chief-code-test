
# Chief-Code-Test

This project implements a Slack bot that uses OpenAI's GPT model for generating responses and can perform function calling, specifically for getting weather information.

## Project Structure

The project is organized as follows:

- `main.py`: The entry point of the application.
- `slackbot.py`: Contains the main bot logic.
- `config.py`: Handles configuration and environment variables.
- `test_slackbot.py`: Contains all the unit tests.
- `requirements.txt`: Lists all the Python dependencies.
- `.env`: Stores environment variables (this file should be in .gitignore).

## Setup

1. Clone the repository:

git clone https://github.com/yourusername/chief-code-test.git
cd chief-code-test

3. Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate

4.Install the required dependencies:
pip install -r requirements.txt

OPENAI_API_KEY=your_openai_api_key
SLACK_BOT_TOKEN=your_slack_bot_token
SLACK_APP_TOKEN=your_slack_app_token
CopyReplace the placeholder values with your actual API keys and tokens.

## Usage

To run the Slack bot:
python main.py

The bot will start and connect to your Slack workspace. It will respond to messages and use OpenAI's GPT model to generate responses. If a user asks about the weather, it will attempt to use the `get_weather` function to provide weather information.

## Running Tests

To run the unit tests:
Certainly! Here's the complete README.md file for your project:
markdownCopy# Chief-Code-Test

This project implements a Slack bot that uses OpenAI's GPT model for generating responses and can perform function calling, specifically for getting weather information.

## Project Structure

The project is organized as follows:

- `main.py`: The entry point of the application.
- `slackbot.py`: Contains the main bot logic.
- `config.py`: Handles configuration and environment variables.
- `test_slackbot.py`: Contains all the unit tests.
- `requirements.txt`: Lists all the Python dependencies.
- `.env`: Stores environment variables (this file should be in .gitignore).

## Setup

1. Clone the repository:
   
git clone https://github.com/yourusername/chief-code-test.git
cd chief-code-test

2. Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate


3. Install the required dependencies:
pip install -r requirements.txt

## Set up your environment variables:
Create a `.env` file in the root directory with the following content:

- OPENAI_API_KEY=your_openai_api_key
- SLACK_BOT_TOKEN=your_slack_bot_token
- SLACK_APP_TOKEN=your_slack_app_token

## Usage

To run the Slack bot:
python main.py
Copy
The bot will start and connect to your Slack workspace. It will respond to messages and use OpenAI's GPT model to generate responses. If a user asks about the weather, it will attempt to use the `get_weather` function to provide weather information.

## Running Tests

To run the unit tests:
python -m unittest test_slackbot.py

This will run all the tests defined in `test_slackbot.py`.

## Development

- To modify the bot's behavior, edit the `SlackBot` class in `slackbot.py`.
- To add new functions for the OpenAI model to call, add them to the `functions` list in `slackbot.py`.
- To change configuration, modify `config.py`.
- When adding new features, make sure to add corresponding unit tests in `test_slackbot.py`.




