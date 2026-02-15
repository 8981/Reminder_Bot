from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from states.reminder_state import ReminderState
from services.reminder_service import create_reminder
from datetime import datetime

router = Router()


@router.message(Command("remind"))
async def cmd_remind(message: types.Message, state: FSMContext):
    await message.answer("Введите текст напоминания")
    await state.set_state(ReminderState.text)


@router.message(ReminderState.text)
async def get_text(message: types.Message, state: FSMContext):
    await state.update_data(text=message.text)
    await message.answer("Введите дату YYYY-MM-DD HH:MM")
    await state.set_state(ReminderState.date)


@router.message(ReminderState.date)
async def get_date(message: types.Message, state: FSMContext):

    try:
        dt = datetime.strptime(message.text, "%Y-%m-%d %H:%M")
    except:
        await message.answer("Неверный формат")
        return

    data = await state.get_data()

    await create_reminder(
        message.from_user.id,
        data["text"],
        dt.isoformat()
    )

    await message.answer("Напоминание сохранено")
    await state.clear()

