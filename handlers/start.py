from aiogram import Router, types
from aiogram.filters import CommandStart
from database.db import add_user, update_user
from config import ADMINS
from keyboards.admin import admin_kb

router = Router()

@router.message(CommandStart())
async def start_handler(message: types.Message):
    user = message.from_user

    await add_user(
        user.id,
        user.username,
        user.full_name
    )

    await update_user(user.id, user.username, user.full_name)

    if user.id in ADMINS:
        await message.answer("Вы администратор", reply_markup=admin_kb)
    else:
        await message.answer("Вы зарегистрированы в системе уведомлений.")
