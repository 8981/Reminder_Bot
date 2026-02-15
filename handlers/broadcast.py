from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from states.broadcast_state import BroadcastState
from services.user_service import get_all_users
from config import ADMINS

router = Router()


@router.callback_query(F.data == "broadcast")
async def broadcast_start(callback: types.CallbackQuery, state: FSMContext):

    if callback.from_user.id not in ADMINS:
        return

    await callback.message.answer("Введите текст рассылки:")
    await state.set_state(BroadcastState.waiting_text)


@router.message(BroadcastState.waiting_text)
async def send_broadcast(message: types.Message, state: FSMContext):

    if message.from_user.id not in ADMINS:
        return

    users = await get_all_users()
    text = message.text
    bot = message.bot

    sent_count = 0

    for user_id in users:
        try:
            await bot.send_message(user_id, text)
            sent_count += 1
        except Exception as e:
            print(f"Ошибка отправки {user_id}: {e}")

    await message.answer(f"Рассылка завершена.\nОтправлено: {sent_count}")
    await state.clear()
