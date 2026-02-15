import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from database.connection import init_db
from scheduler.reminder_scheduler import reminder_scheduler

from handlers import start, reminders, broadcast

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

dp.include_router(start.router)
dp.include_router(reminders.router)
dp.include_router(broadcast.router)

async def main():
    await init_db()

    asyncio.create_task(reminder_scheduler(bot))

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
