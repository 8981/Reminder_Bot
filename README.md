# 📢 Telegram Reminder & Broadcast Bot

## 📌 Description

This project is a Telegram bot built with **aiogram 3** that supports:

* user registration
* admin broadcasts
* personal reminders
* background scheduler
* clean architecture (handlers → services → repositories → database)

It is designed as a production-ready template for scalable Telegram bots.

---

## ⚙️ Tech Stack

* Python 3.11+
* aiogram 3
* SQLite (aiosqlite)
* asyncio
* FSM states

---

## 📁 Project Structure

```
project/
│
├── handlers/        # message handlers
├── services/        # business logic
├── repositories/    # database queries
├── database/        # connection + initialization
├── scheduler/       # background tasks
├── states/          # FSM states
├── keyboards/       # keyboards
├── config.py        # configuration
└── main.py          # entry point
```

---

## 🚀 Run Project

### 1️⃣ Install dependencies

```
pip install aiogram python-dotenv aiosqlite
```

---

### 2️⃣ Create `.env`

```
BOT_TOKEN=your_token_here
ADMIN_IDS=123456789,987654321
```

---

### 3️⃣ Run

```
python main.py
```

---

## 👤 User Registration

Any user is automatically registered after running:

```
/start
```

Stored data:

* telegram id
* username
* full name

---

## 📢 Broadcast (Admin only)

Admin presses:

```
📢 Broadcast
```

Then enters text → bot sends message to all users.

---

## ⏰ Reminders

Command:

```
/remind
```

Bot asks for:

1. text
2. date in format

```
YYYY-MM-DD HH:MM
```

When the time comes — the bot sends a reminder.

---

## 🔁 Scheduler

Background task runs every 30 seconds:

* checks due reminders
* sends messages
* deletes completed reminders

---

## 🧠 Layered Architecture

### handlers

Receive updates and call services.

### services

Application business logic.

### repositories

Pure SQL logic.

### database

Initialization and connection.

---

## 🗄 Database Schema

### users

| field       | type |
| ----------- | ---- |
| id          | int  |
| telegram_id | int  |
| username    | text |
| full_name   | text |

### reminders

| field     | type |
| --------- | ---- |
| id        | int  |
| user_id   | int  |
| text      | text |
| remind_at | text |

---

## 🛡 Security

Broadcasts are available only to users listed in `ADMIN_IDS`.

---

## 📈 Future Improvements

Easy to extend with:

* admin web panel
* delivery statistics
* broadcast templates
* scheduled broadcasts
* Redis FSM storage
* PostgreSQL

---

## 👨‍💻 Author

Built as a scalable Telegram bot template with clean architecture.

---

## ⭐ Recommendation

Before using in production, consider adding:

* logging
* retry logic for message sending
* Telegram rate-limit handling
