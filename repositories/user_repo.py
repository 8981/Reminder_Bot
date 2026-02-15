from database.connection import get_db


async def add_user(user_id, username, full_name):
    db = await get_db()
    await db.execute(
        "INSERT OR IGNORE INTO users (telegram_id, username, full_name) VALUES (?, ?, ?)",
        (user_id, username, full_name)
    )
    await db.commit()
    await db.close()


async def update_user(user_id: int, username: str, full_name: str):
    db = await get_db()
    await db.execute("""
        UPDATE users
        SET username = ?, full_name = ?
        WHERE telegram_id = ?
    """, (username, full_name, user_id))
    await db.commit()

async def get_all_users():
    db = await get_db()
    cur = await db.execute("SELECT telegram_id FROM users")
    rows = await cur.fetchall()
    await db.close()
    return [r[0] for r in rows]

