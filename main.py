import asyncio
from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from database.db import int_db
from handlers import start, broadcast

async def main():
    await int_db()

    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(broadcast.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
