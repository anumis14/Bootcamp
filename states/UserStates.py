from aiogram.fsm.state import StatesGroup, State


class UserInfo(StatesGroup):
    name = State()
    surname = State()
    age = State()
    description = State()
    photo = State()