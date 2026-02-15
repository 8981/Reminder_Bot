import asyncio
from services.reminder_service import get_ready_reminders, remove_reminder


async def reminder_scheduler(bot):

    while True:
        reminders = await get_ready_reminders()

        for r in reminders:
            rid, uid, text = r
            await bot.send_message(uid, f"⏰ Напоминание:\n{text}")
            await remove_reminder(rid)

        await asyncio.sleep(30)

