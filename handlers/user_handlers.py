
from aiogram import F, Router
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State
from aiogram.types import Message, CallbackQuery

from states.UserStates import UserInfo
from keyboards.keyboards import yn_kb, menu_kb
from handlers.texts import menu_text
router = Router()



@router.message(CommandStart(), StateFilter(default_state))
async def start_cmd(message: Message, state: FSMContext):
    await state.set_state(UserInfo.name)
    await message.answer("Добро пожаловать. Напишите свое имя.")


@router.message(Command("menu"), StateFilter(default_state))
async def menu_cmd(message: Message):
    await message.answer(text=menu_text, reply_markup=menu_kb)


@router.message(StateFilter(UserInfo.name))
async def name_cmd(message: Message, state: FSMContext):
    user_data = await state.update_data(name=message.text)
    name = user_data["name"]
    await state.set_state(UserInfo.surname)
    await message.answer(f"{name}, отлично, теперь напишите фамилию.")

@router.message(StateFilter(UserInfo.surname))
async def name_cmd(message: Message, state: FSMContext):
    user_data = await state.update_data(surname=message.text)
    await state.set_state(UserInfo.age)
    await message.answer("Отлично, теперь напишите свой возраст.")

@router.message(StateFilter(UserInfo.age))
async def age_cmd(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(UserInfo.description)
    await message.answer("Напишите о себе, чем вы занимаетесь и чем увлекаетесь.")

@router.message(StateFilter(UserInfo.description))
async def description_cmd(message: Message, state: FSMContext):
    await state.update_data(user_description=message.text)
    await state.set_state(UserInfo.photo)
    await message.answer("Отправьте фотографию профиля.")


# @router.message(StateFilter(UserInfo.age))
# async def age_cmd(message: Message, state: FSMContext):
#     await state.update_data(age=message.text)
#     await state.set_state(UserInfo.photo)
#     await message.answer("Отправьте фотографию профиля")


@router.message(StateFilter(UserInfo.photo))
async def photo_cmd(message: Message, state: FSMContext):
    user_data = await state.update_data(profile_photo=message.photo[-1].file_id)
    age, name, surname = user_data["age"], user_data["name"], user_data["surname"]
    await message.answer_photo(caption=f"Фамилия имя: {surname} {name}\n"
                         f"Возраст: {age}. Всё верно?", reply_markup=yn_kb, photo=user_data["profile_photo"])



@router.callback_query(F.data == "yes_btn")
async def choices_cmd(call: CallbackQuery, state: FSMContext):
    await call.answer("Отлично. Приятного использования", show_alert=False)
    await call.message.delete()
    await call.message.answer("Привет это бот", reply_markup=menu_kb)
    await state.clear()

@router.callback_query(F.data == "no_btn")
async def choices_cmd(call: CallbackQuery, state: FSMContext):
    await state.set_state(UserInfo.name)
    await call.answer("Заполните анкету заново")
    await call.message.answer("Напишите свое имя")

