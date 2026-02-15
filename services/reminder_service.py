from repositories.reminder_repo import (
    add_reminder,
    get_due_reminders,
    delete_reminder
)
from datetime import datetime, timezone


async def create_reminder(user_id: int, text: str, date: str) -> None:
    try:
        datetime.fromisoformat(date)
    except ValueError:
        raise ValueError("Invalid date format")

    await add_reminder(user_id, text, date)


async def get_ready_reminders():
    now = datetime.now(timezone.utc).isoformat()
    return await get_due_reminders(now)


async def remove_reminder(reminder_id: int):
    await delete_reminder(reminder_id)
