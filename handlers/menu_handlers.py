from aiogram import F, Router
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup

from states.UserStates import UserInfo
from keyboards.keyboards import bw_btn, menu_kb, profile_menu, study_menu, to_study_menu
from keyboards.keyboards import zapis, to_menu_btn
from handlers.texts import menu_text

router = Router()

@router.callback_query(F.data == "menu_btn")
async def to_menu_cmd(call: CallbackQuery):
    await call.message.edit_text(text=menu_text,reply_markup=menu_kb)

@router.callback_query(F.data == "profile_btn")
async def to_menu_cmd(call: CallbackQuery):
    await call.message.edit_text(text="Имя: Петя\n"
                                         "Возраст: 20\n"
                                         "Люблю математику и прогу",reply_markup=profile_menu)

@router.callback_query(F.data == "study_btn")
async def to_menu_cmd(call: CallbackQuery):
    await call.message.edit_text(text="Все учебные мероприятия↴ ",reply_markup=study_menu)

@router.callback_query(F.data == "study_btn1")
async def to_menu_cmd(call: CallbackQuery):
    await call.message.edit_text(text="Время: 10.02.2025\n"
                                      "Место: 1 кампус ЦУ",reply_markup=InlineKeyboardMarkup(inline_keyboard=[[zapis], [to_menu_btn]]))
    await call.message.answer_photo(photo="https://storage.yandexcloud.net/moskvichmag/uploads/2023/08/gasheka-7.png")

@router.callback_query(F.data == "to_menu_btn")
async def to_menu_cmd(call: CallbackQuery):
    await call.message.edit_text(text="Все учебные мероприятия↴ ",reply_markup=study_menu)


@router.callback_query(F.data == "support_btn")
async def choices_cmd(call: CallbackQuery):
    await call.message.edit_text("↳Техподдержка: @support", reply_markup=InlineKeyboardMarkup(inline_keyboard=[[bw_btn]]))


