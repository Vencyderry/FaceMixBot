import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types.web_app_info import WebAppInfo

logging.basicConfig(level=logging.INFO)

bot = Bot(token="7241327179:AAHCfUdwV83Iqnvn6JGLZkOLZWoiT8LZ-5A")

dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text='Открыть приложение', web_app=WebAppInfo(url="http://localhost:63342/FaceMixBot/application.html?_ijt=p8hd04kvsbcmsa6t0c8ifs56s1&_ij_reload=RELOAD_ON_SAVE"))]
    ]
    markup = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Hello!", reply_markup=markup)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())