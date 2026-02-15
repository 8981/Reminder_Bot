from aiogram import Router, types
from aiogram.filters import CommandStart
from repositories.user_repo import add_user, update_user
from config import ADMINS
from keyboards.admin import admin_kb

router = Router()


@router.message(CommandStart())
async def start_handler(message: types.Message):

    await add_user(
        message.from_user.id,
        message.from_user.username,
        message.from_user.full_name
    )

    await update_user(
        message.from_user.id, 
        message.from_user.username, 
        message.from_user.full_name
    )

    if message.from_user.id in ADMINS:
        await message.answer("Вы администратор", reply_markup=admin_kb)
    else:
        await message.answer("Вы зарегистрированы.")
