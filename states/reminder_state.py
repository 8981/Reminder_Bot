from aiogram.fsm.state import State, StatesGroup


class ReminderState(StatesGroup):
    text = State()
    date = State()
