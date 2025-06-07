import unittest
from unittest.mock import patch, MagicMock
from aiogram import types
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from telegram_bot.bot import (
    dp,
    evaluate_user_behavior,
    send_welcome,
    send_info,
    evaluate_behavior,
)

class TestBot(unittest.TestCase):

    @patch('bot.evaluate_user_behavior', return_value='good')
    async def test_evaluate_behavior_good(self, mock_evaluate):
        message = types.Message(message_id=1, from_user=types.User(id=1, is_bot=False, first_name='Test'),
                                chat=types.Chat(id=1, type='private'), date=0, text='/evaluate')
        message.reply = MagicMock()
        await evaluate_behavior(message)
        mock_evaluate.assert_called_once()
        message.reply.assert_called_with("Comrade, you are behaving excellently! Request to issue Koshka Jena has been submitted.")

    @patch('bot.evaluate_user_behavior', return_value='bad')
    async def test_evaluate_behavior_bad(self, mock_evaluate):
        message = types.Message(message_id=1, from_user=types.User(id=1, is_bot=False, first_name='Test'),
                                chat=types.Chat(id=1, type='private'), date=0, text='/evaluate')
        message.reply = MagicMock()
        await evaluate_behavior(message)
        mock_evaluate.assert_called_once()
        message.reply.assert_called_with("Comrade, you need to improve your behavior to be a good party member.")

if __name__ == '__main__':
    unittest.main()

