from database.connection import get_db


async def add_reminder(user_id, text, remind_at):
    db = await get_db()
    await db.execute(
        "INSERT INTO reminders (user_id,text,remind_at) VALUES (?,?,?)",
        (user_id, text, remind_at)
    )
    await db.commit()
    await db.close()


async def get_due_reminders(now):
    db = await get_db()
    cur = await db.execute(
        "SELECT id,user_id,text FROM reminders WHERE remind_at<=?",
        (now,)
    )
    rows = await cur.fetchall()
    await db.close()
    return rows


async def delete_reminder(reminder_id):
    db = await get_db()
    await db.execute("DELETE FROM reminders WHERE id=?", (reminder_id,))
    await db.commit()
    await db.close()
