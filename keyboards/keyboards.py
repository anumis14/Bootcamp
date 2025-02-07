from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

yes_btn = InlineKeyboardButton(text="Да", callback_data="yes_btn")
no_btn = InlineKeyboardButton(text="Нет", callback_data="no_btn")
yn_kb = InlineKeyboardMarkup(row_width=2, inline_keyboard=[[yes_btn], [no_btn]])


profile_btn = InlineKeyboardButton(text="Профиль", callback_data="profile_btn")
fun_btn = InlineKeyboardButton(text="Развлечения", callback_data="fun_btn")
obeds_btn = InlineKeyboardButton(text="Обеды", callback_data="obeds_btn")
sport_btn = InlineKeyboardButton(text="Спорт", callback_data="sport_btn")
study_btn = InlineKeyboardButton(text="Учёба", callback_data="study_btn")
category_btn = InlineKeyboardButton(text="Категории", callback_data="category_btn")
support_btn = InlineKeyboardButton(text="Техподдержка", callback_data="support_btn")
menu_kb = InlineKeyboardMarkup(row_width=3, inline_keyboard=[
    [profile_btn], [study_btn, obeds_btn],[sport_btn, fun_btn], [support_btn]])

first_study = InlineKeyboardButton(text="Боталка матана", callback_data="study_btn1")

zapis = InlineKeyboardButton(text="Записаться", callback_data="zapis_btn")

to_menu_btn = InlineKeyboardButton(text="Назад", callback_data="to_menu_btn")
bw_btn = InlineKeyboardButton(text="Назад", callback_data="menu_btn")

profile_menu = InlineKeyboardMarkup(inline_keyboard=[[bw_btn]])

study_menu = InlineKeyboardMarkup(inline_keyboard=[[first_study],[bw_btn]])
to_study_menu = InlineKeyboardMarkup(inline_keyboard=[[to_menu_btn]])
# study_menu = InlineKeyboardMarkup