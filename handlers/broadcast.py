from itertools import count
from pydoc import text
from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import user
from database.db import get_all_users
from config import ADMINS


router = Router()

class BroadcastState(StatesGroup):
    waiting_text = State()


@router.callback_query(F.data == "broadcast")
async def broadcast_start(callback: types.CallbackQuery, state: FSMContext):
    if callback.from_user.id not in ADMINS:
        return

    await callback.message.answer("Введите текст рассылки:")
    await state.set_state(BroadcastState.waiting_text)

@router.message(BroadcastState.waiting_text)
async def send_broadcast(message: types.Message, state: FSMContext, bot):
    if message.from_user.id not in ADMINS:
        return

    users = await get_all_users()
    text = message.text

    count = 0
    for user_id in users:
        try:
            await bot.send_message(user_id, text)
            count += 1
        except:
            pass


    await message.answer(f"Рассылка завершена. Отправлено: {count}")
    await state.clear()