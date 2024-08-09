import unittest
from unittest.mock import patch, MagicMock
from slackbot import SlackBot

class TestSlackBot(unittest.TestCase):
    def setUp(self):
        self.bot = SlackBot()

    @patch('openai.OpenAI')
    def test_call_openai_no_function_call(self, mock_openai):
        # Arrange
        mock_response = MagicMock()
        mock_response.choices = [
            MagicMock(
                function_call=None, 
                message=MagicMock(content="This is a test response")
            )
        ]
        mock_openai.return_value.chat.completions.create.return_value = mock_response

        # Act
        response = self.bot.call_openai("What's the meaning of life?")

        # Assert
        self.assertEqual(response, "This is a test response")
        mock_openai.return_value.chat.completions.create.assert_called_once()

    @patch('openai.OpenAI')
    def test_call_openai_with_function_call(self, mock_openai):
        # Arrange
        mock_response1 = MagicMock()
        mock_response1.choices = [
            MagicMock(
                function_call=MagicMock(
                    name="get_weather", 
                    arguments='{"location": "New York"}'
                )
            )
        ]
        
        mock_response2 = MagicMock()
        mock_response2.choices = [
            MagicMock(
                message=MagicMock(content="The weather in New York is sunny.")
            )
        ]
        
        mock_openai.return_value.chat.completions.create.side_effect = [mock_response1, mock_response2]

        # Act
        with patch('slackbot.get_weather', return_value="Sunny weather in New York") as mock_get_weather:
            response = self.bot.call_openai("What's the weather in New York?")

        # Assert
        self.assertEqual(response, "The weather in New York is sunny.")
        self.assertEqual(mock_openai.return_value.chat.completions.create.call_count, 2)
        mock_get_weather.assert_called_once_with("New York")

    @patch('slack_bolt.App.message')
    def test_handle_message(self, mock_message):
        # Arrange
        mock_say = MagicMock()
        mock_message.return_value({"text": "Hello"}, say=mock_say)
        
        # Act
        with patch.object(self.bot, 'call_openai', return_value="Hello, how can I help you?") as mock_call_openai:
            self.bot.app.message(".*")({"text": "Hello"}, mock_say)
        
        # Assert
        mock_call_openai.assert_called_once_with("Hello")
        mock_say.assert_called_once_with("Hello, how can I help you?")

if __name__ == "__main__":
    unittest.main()
