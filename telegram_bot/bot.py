import logging
import os
import asyncio
import json
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

def load_reply(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read()

def load_keyboard(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        buttons = json.load(file)
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text=button["text"], callback_data=button["callback_data"])]
            for button in buttons
        ])
        return keyboard

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    start_reply = load_reply('Replies/start_reply.txt')
    keyboard = load_keyboard('Keyboards/start_keyboard.json')
    await message.reply(start_reply, reply_markup=keyboard)

@dp.message(Command("help"))
async def send_help(message: types.Message):
    help_reply = load_reply('Replies/help_reply.txt')
    await message.reply(help_reply)

@dp.message(Command("info"))
async def send_info(message: types.Message):
    info_reply = load_reply('Replies/info_reply.txt')
    await message.reply(info_reply)

@dp.callback_query(lambda c: c.data in ["yes", "no"])
async def process_callback(callback_query: types.CallbackQuery):
    if callback_query.data == "yes":
        response = load_reply('Replies/yes_callback.txt')
    else:
        response = load_reply('Replies/no_callback.txt')
    await callback_query.message.answer(response)
    await callback_query.answer()

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
