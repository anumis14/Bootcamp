import asyncio
import os

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from dotenv import load_dotenv

from handlers import user_handlers, menu_handlers

async def main() -> None:
    load_dotenv()
    bot_token = os.getenv("TG_BOT_TOKEN")

    dp = Dispatcher()
    dp.include_router(user_handlers.router)
    dp.include_router(menu_handlers.router)
    # dp.message.register(echo, F.text)

    bot = Bot(token=bot_token)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())