import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import os
from dotenv import load_dotenv

# Завантаження токена з .env
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Налаштування клавіатури
keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Слава Україні")]], resize_keyboard=True)

@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer("Вітаю! Натисніть кнопку, щоб продовжити.", reply_markup=keyboard)

@dp.message(lambda message: message.text == "Слава Україні")
async def reply_to_glory(message: types.Message):
    await message.answer("Героям слава!")

async def run_bot():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)
