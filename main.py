import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import config

API_TOKEN = config.token

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer("Привет! Я эхобот на aiogram 3. Отправь мне любое сообщение, и я повторю его.")

@dp.message(Command("info"))
async def command_info(message: types.Message):
    await message.answer("Это команда info. Здесь вы можете получить информацию о боте.")

@dp.message(Command("help"))
async def command_help(message: types.Message):
    await message.answer("Это команда help. Здесь вы можете получить помощь по командам бота.")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

