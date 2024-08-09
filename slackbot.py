import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from openai import OpenAI
import json
from config import OPENAI_API_KEY, SLACK_BOT_TOKEN, SLACK_APP_TOKEN

class SlackBot:
    def __init__(self):
        self.app = App(token=SLACK_BOT_TOKEN)
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        
        @self.app.message(".*")
        def handle_message(message, say):
            response = self.call_openai(message["text"])
            say(response)
    
    def call_openai(self, message):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo-0613",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message}
            ],
            functions=functions,
            function_call="auto"
        )

        if response.choices[0].function_call:
            function_call = response.choices[0].function_call
            
            if function_call.name == "get_weather":
                # Parse the location from the function call arguments
                args = json.loads(function_call.arguments)
                location = args.get("location")
                
                function_response = get_weather(location)
                
                second_response = self.client.chat.completions.create(
                    model="gpt-3.5-turbo-0613",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": message},
                        {"role": "function", "name": function_call.name, "content": function_response}
                    ]
                )
                return second_response.choices[0].message.content
        else:
            return response.choices[0].message.content

    def start(self):
        SocketModeHandler(self.app, SLACK_APP_TOKEN).start()

def get_weather(location):
    # This is a placeholder. In a real application, you'd call a weather API here.
    # For demonstration purposes, we'll return a static response.
    return f"The weather in {location} is currently sunny with a high of 75°F (24°C) and a low of 60°F (16°C). There's a 10% chance of rain."

# Define the available functions for OpenAI function calling
functions = [
    {
        "name": "get_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The city and state, e.g. San Francisco, CA",
                },
            },
            "required": ["location"],
        },
    }
]
