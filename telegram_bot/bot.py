import logging
import random
import os
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm your friendly Telegram bot!\nUse /info to get more information.")

@dp.message_handler(commands=['info'])
async def send_info(message: types.Message):
    await message.reply("This bot is created using aiogram library. It can respond to /start, /help, and /info commands.")

@dp.message_handler(commands=['evaluate'])
async def evaluate_behavior(message: types.Message):
    user_behavior = evaluate_user_behavior()
    if user_behavior == "good":
        await message.reply("Comrade, you are behaving excellently! Request to issue Koshka Jena has been submitted.")
    else:
        await message.reply("Comrade, you need to improve your behavior to be a good party member.")

def evaluate_user_behavior():
    # Simple random evaluation for demonstration
    return random.choice(["good", "bad"])

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
